from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from timeline.models import Post
from timeline.forms import PostForm
from django.contrib import messages
from friends.models import Friends

# Create your views here.

@login_required
def home(request):
    return render(request, 'home/home.html')

@login_required
def home2(request):
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
        posts = Post.objects.all().order_by(
            '-date_posted')
        try:
            friend = Friends.objects.get(current_user=request.user)
            friends = friend.users.all()
        except Friends.DoesNotExist:
            return HttpResponse(render(request,
                                       "home/admin_restrictions.html"))
        context = {'posts': posts,'form':form,'friends':friends}
        return render(request, 'home/home2.html', context)


