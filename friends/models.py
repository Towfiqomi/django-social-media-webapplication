from django.db import models
from django.contrib.auth.models import User


# Create your models here.

#
# class Post(models.Model):
#     post = models.CharField(max_length=500)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)


class FriendRequest(models.Model):
    users = models.ManyToManyField(User)
    c_user = models.ForeignKey(User, related_name='my', null=True, on_delete=models.CASCADE)

    @classmethod
    def make_friend_request(cls, current_user, new_friend_req):
        friend, created = cls.objects.get_or_create(
            c_user=new_friend_req
        )
        print(current_user)
        print(new_friend_req)
        friend.users.add(current_user)

    @classmethod
    def reject_friend_request(cls, current_user, new_friend_req):
        friend, created = cls.objects.get_or_create(
            c_user=current_user
        )
        friend.users.remove(new_friend_req)


class Friends(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner', null=True, on_delete=models.CASCADE)

    @classmethod
    def make_friend_request_accept(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)
