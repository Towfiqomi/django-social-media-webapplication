from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from discussion.forms import DiscussionForm
from django.contrib import messages
from .models import CreateDiscussion
from .models import DiscussionMessage
from friends.models import Friends

from django.utils.timezone import utc

import datetime


def create_discussion(request):
    if request.method == "POST":
        form = DiscussionForm(request.POST)
        if form.is_valid():
            createDiscussionTable = CreateDiscussion()
            createDiscussionTable.discussion_title = request.POST['discussion_title']
            createDiscussionTable.discussion_created = request.user
            createDiscussionTable.save()
        messages.success(request,
                         f'Discussion Created Successfully!')
        return redirect('discussion')
    else:
        form = DiscussionForm()
        discussions = CreateDiscussion.objects.all().order_by('-discussion_time_stamp')
        try:
            friend = Friends.objects.get(current_user=request.user)
            friends = friend.users.all()
        except Friends.DoesNotExist:
            return HttpResponse(render(request,
                                       "home/admin_restrictions.html"))

        context = {'form': form, 'discussions': discussions, 'friends': friends}
        return render(request, 'discussion/discussion.html', context)


def view_discussions(request, pk):
    discussions = CreateDiscussion.objects.get(pk=pk)
    chats = DiscussionMessage.objects.filter(discussion_id_id=pk)
    friend = Friends.objects.get(current_user=request.user)
    friends = friend.users.all()
    context = {'discussion': discussions, 'all_messages': chats,'friends':friends}

    return render(request, "discussion/discussion-detail.html", context)


def message_send(request):

    if request.method == 'GET':

        send_message = DiscussionMessage()
        send_message.discussion_id_id = request.GET['discussion_id']
        send_message.message_sender_id = request.user.id
        send_message.message = request.GET['message_text']
        send_message.message_time = datetime.datetime.now().strftime('%H:%M:%S')

        send_message.save()

    return HttpResponse(1)


def message_save_view(request):

    discussion_id = request.GET['discussion_id']
    messages = DiscussionMessage.objects.filter(discussion_id_id=discussion_id)

    return render(request, 'discussion/message_sending_view.html', {'messages': messages})


def message_delete_view(request):

    if request.method == 'GET':

        message = DiscussionMessage.objects.filter(id=request.GET['message_id'])
        message.delete()

    return HttpResponse(1)

