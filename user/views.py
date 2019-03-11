from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User
from friends.models import Friends
from timeline.models import Post
from discussion.models import CreateDiscussion, DiscussionMessage

from . import models


def register(request):
    if request.method == 'POST':
        # return HttpResponse(request.POST.get('password1'))
        form = UserRegistrationForm(request.POST)
        # profileForm = UserUpdateForm(request.POST)
        if form.is_valid():
            userTable = models.User()
            userTable.first_name = request.POST['first_name']
            userTable.last_name = request.POST['last_name']
            userTable.username = request.POST['username']
            userTable.email = request.POST['email']
            userTable.password = make_password(request.POST.get('password1'))
            userTable.save()

            friendTable = Friends()
            friendTable.current_user = userTable
            friendTable.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login!')
            messages.warning(request,
                             f'Please login to your account and update profile using [Edit Profile] option!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
        # profileForm = UserUpdateForm()
    return render(request, 'user/registration.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,
                                instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile is updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'user/profile.html', context)


@login_required
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
        posts = Post.objects.filter(user=request.user).order_by(
            '-date_posted')
        discussions = CreateDiscussion.objects.filter(
            discussion_created=request.user)
        all_messages = DiscussionMessage.objects.filter(
            message_sender=request.user).distinct('discussion_id')
        print(user)
    else:
        user = request.user
        print(user)
    context = {'user': user, 'posts':posts, 'discussions':discussions, 'all_messages':all_messages}
    return render(request, "user/view_profile.html", context)

@login_required
def view_profile2(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
        print(user)
    else:
        user = request.user
        print(user)
    context = {'user': user}
    return render(request, "user/view_profile2.html", context)

@login_required
def view_profile_full(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
        print(user)
    else:
        user = request.user
        print(user)
    context = {'user': user}
    return render(request, "user/view_profile_full.html", context)

def delete_account(request):
    return render(request,'user/delete_account.html')

def delete_account2(request):
    User.objects.filter(pk=request.user.pk).delete()
    User.objects.filter(pk=request.user.pk).update(is_active=False, email=None)
    messages.success(request,
                     f'Your account has been deleted!')
    return HttpResponseRedirect(reverse('logout'))

