from django.shortcuts import render, redirect
from .models import Post
from timeline.forms import PostForm
from django.contrib import messages
from friends.models import Friends

# Create your views here.

def createPost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            postTable = Post()
            postTable.content = request.POST['content']
            postTable.user = request.user
            postTable.save()
        messages.success(request,
                         f'Status has been updated')
        return redirect('home2')
    else:
        form = PostForm()
        return render(request, 'home/home2.html', {'form':form})

def viewPost(request):
    posts = Post.objects.all().order_by(
        '-date_posted')
    friend = Friends.objects.get(current_user=request.user)
    friends = friend.users.all()
    context = {'posts': posts, 'friends': friends}
    return render(request, 'timeline/status.html', context)

# def viewSelfPost(request):
#     posts = Post.objects.filter(user=request.user).order_by(
#         '-date_posted')
#     context = {'posts': posts}
#     return render(request, 'timeline/my_statuses.html', context)

