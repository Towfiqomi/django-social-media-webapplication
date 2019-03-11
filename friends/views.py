from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.models import User
from friends.models import Friends, FriendRequest
from django.shortcuts import get_object_or_404
from user.models import Profile
from django.http import HttpResponse

from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
# Create your views here.


# def friend_list(request):
#     normal_users = User.objects.exclude(id=request.user.id).exclude(username="admin")
#     user_image = Profile.image
#
#     return render(request, "friends/friends.html", {
#         'normal_users': normal_users,
#         'user_image': user_image
#     })


def timeline(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    context = {'user': user}
    return render(request, 'friends/timeline.html', context)


# def view_friends(request):
#     users = User.objects.exclude(id=request.user.id).exclude(username="admin")
#     friend = Friends.objects.filter(current_user=request.user)
#     friends = friend.users.all()
#
#     context = {
#         "users": users,
#         "friends": friends
#     }
#     return render(request, 'friends/searchfriends.html', context)

def timeline_find_friends(request):
    # friendss = Friends.objects.get(current_user=request.user)
    # notfriend = friendss.users.exclude(friendrequest__users=True, friends__current_user__username=True)
    # context = {
    #     "notfriend": notfriend
    # }
    # return render(request, 'friends/timeline-findfriends.html', context)
    try:
        users = User.objects.exclude(id=request.user.id).exclude(username="admin")
        friend = Friends.objects.get(current_user=request.user)
        # friend = get_object_or_404(Friends,current_user=request.user)
        friends = friend.users.all()
        context = {
            "users": users,
            "friends": friends,
        }
        return render(request, 'friends/searchfriends.html', context)
    except Friends.DoesNotExist:
        users = User.objects.exclude(id=request.user.id).exclude(
            username="admin")
        friend = Friends.objects.filter(current_user=request.user)
        # friend = get_object_or_404(Friends,current_user=request.user)
        friends = friend.all()
        context = {
            "users": users,
            "friends": friends,
        }
        return render(request, 'friends/searchfriends.html', context)


def friend_request_list(request):
    try:
        friend = FriendRequest.objects.get(c_user=request.user)
        friends = Friends.objects.get(current_user=request.user)
    except FriendRequest.DoesNotExist:
        return HttpResponse(render(request,"friends/no_friend_requests.html"))
    except Friends.DoesNotExist:
        return HttpResponse(render(request,"friends/no_friend_requests.html"))

    friend1 = friend.users.all()
    friend2 = friends.users.all()

    context = {
        "friend_req_list": friend1,
        "friends": friend2,
    }

    return render(request, 'friends/friend_request_list.html', context)


def timeline_friends(request):
    try:
        friend = Friends.objects.get(current_user=request.user)

    except Friends.DoesNotExist:
        return HttpResponse(render(request,"friends/no_friends.html"))

    friends = friend.users.all()
    context = {
        "viewfriends": friends
    }

    return render(request, 'friends/timeline-friends.html', context)

def friends_relation(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'req':
        FriendRequest.make_friend_request(request.user, friend)
    elif operation == 'rej':
        FriendRequest.reject_friend_request(request.user, friend)
    elif operation == 'add':
        Friends.make_friend_request_accept(request.user, friend)
        Friends.make_friend_request_accept(friend, request.user)
    elif operation == 'remove':
        Friends.lose_friend(request.user, friend)
        Friends.lose_friend(friend, request.user)
    return redirect('home2')