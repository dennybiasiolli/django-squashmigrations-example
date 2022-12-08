from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.utils import DataError, IntegrityError
from django.test import TestCase

from main.models import Like, Tweet


class TweetTestCase(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        self.u1 = UserModel.objects.create(username="foo")
        self.u2 = UserModel.objects.create(username="bar")
        self.t1 = Tweet.objects.create(
            created_by=self.u1,
            text="My first tweet",
        )

    def test_tweet_with_250_chars(self):
        tweet = Tweet.objects.create(
            created_by=self.u1,
            text="a" * 250,
        )
        tweet.full_clean()
        self.assertEqual(len(tweet.text), 250)

    def test_validation_error_creating_tweet_longer_than_250_chars(self):
        def create_fn() -> Tweet:
            return Tweet.objects.create(
                created_by=self.u1,
                text="a" * (250 + 1),
            )

        db_engine = settings.DATABASES["default"]["ENGINE"]
        if db_engine == "django.db.backends.sqlite3":
            tweet = create_fn()
            self.assertRaises(ValidationError, tweet.full_clean)
        elif db_engine == "django.db.backends.postgresql":
            self.assertRaises(DataError, create_fn)

    def test_tweet_like_unique_per_user(self):
        tweet = Tweet.objects.create(
            created_by=self.u1,
            text="a" * 250,
        )
        Like.objects.create(
            tweet=tweet,
            created_by=self.u1,
        )
        Like.objects.create(
            tweet=tweet,
            created_by=self.u2,
        )
        with self.assertRaises(Exception) as raised:
            with transaction.atomic():
                Like.objects.create(
                    tweet=tweet,
                    created_by=self.u2,
                )
        self.assertEqual(IntegrityError, type(raised.exception))
        self.assertEqual(tweet.like_set.count(), 2)
