from django.db import models
from django.utils import timezone


class Post(models.Model):  # models.Model means that the Post is a Django Model, so Django knows it should be saved in the database.
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # link to another model
    title = models.CharField(max_length=200)  # to define a text with a limited number of characters
    text = models.TextField()  # for a text field without a limit of num of characters
    created_date = models.DateTimeField(default=timezone.now) # date and time
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
