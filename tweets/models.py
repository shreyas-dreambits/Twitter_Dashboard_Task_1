from django.db import models
import uuid


class Tweet(models.Model):
    tweeter_user = models.CharField(max_length=30)
    tweet_caption = models.TextField(null=True, blank=True)
    tweet_category = models.CharField(max_length=20)
    tweet_image = models.ImageField(null=True, blank=True)
    tweet_url = models.CharField(max_length=500, null=True, blank=True)
    hashtag_name = models.CharField(max_length=50)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.tweeter_user
