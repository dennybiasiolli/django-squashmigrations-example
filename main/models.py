from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models


class Tweet(models.Model):
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=250, blank=True)
    related_tweet = models.ForeignKey(
        "Tweet", blank=True, null=True, on_delete=models.CASCADE
    )

    def clean(self):
        if not (self.text or self.related_tweet):
            raise ValidationError(
                {
                    "text": ValidationError(
                        "Missing text or related_tweet.", code="invalid"
                    ),
                    "related_tweet": ValidationError(
                        "Missing text or related_tweet.", code="invalid"
                    ),
                }
            )


class Like(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name="likes")
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["tweet", "created_by"]
