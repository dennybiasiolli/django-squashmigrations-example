from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from main.models import Tweet


class TweetTestCase(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        self.u1 = UserModel.objects.create()
        self.t1 = Tweet.objects.create(
            created_by=self.u1,
            text="My first tweet",
        )

    def test_tweet_with_280_chars(self):
        tweet = Tweet.objects.create(
            created_by=self.u1,
            text="a" * 280,
        )
        tweet.full_clean()
        self.assertEqual(len(tweet.text), 280)

    def test_validation_error_creating_tweet_longer_than_280_chars(self):
        tweet = Tweet.objects.create(
            created_by=self.u1,
            text="a" * 281,
        )
        self.assertRaises(ValidationError, tweet.full_clean)
