from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class CreateDiscussion(models.Model):
    discussion_title = models.CharField(max_length=300)
    discussion_created = models.ForeignKey(User, on_delete=models.CASCADE)
    discussion_time_stamp = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('discussion_details', kwargs={'pk': self.pk})


class DiscussionUsers(models.Model):
    discussion_id = models.ForeignKey(CreateDiscussion, on_delete=models.CASCADE)
    discussion_user = models.ForeignKey(User, on_delete=models.CASCADE)


class DiscussionMessage(models.Model):
    discussion_id = models.ForeignKey(CreateDiscussion, on_delete=models.CASCADE)
    message_sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=600)
    message_time = models.DateTimeField(auto_now_add=True)







