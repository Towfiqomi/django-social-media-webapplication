"""bwa2018djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from user import views as user_views
from timeline import views as timeline_views
from discussion import views as discussion_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('delete_account/',user_views.delete_account,name='delete_account'),
    path('delete_account2/',user_views.delete_account2,name='delete_account2'),
    path('timeline/', timeline_views.viewPost, name='timeline_status'),
    path('post/new/', timeline_views.createPost, name='post-create'),
    path('view_profile/<int:pk>/', user_views.view_profile, name="view_profile"),
    path('view_profile2/<int:pk>/', user_views.view_profile2, name="view_profile2"),
    path('view_profile_full/<int:pk>/', user_views.view_profile_full, name="view_profile_full"),
    path('discussion/', discussion_views.create_discussion, name='discussion'),
    path('discussion_details/<int:pk>/', discussion_views.view_discussions, name='discussion_details'),
    path('message_save', discussion_views.message_send, name='message_save'),
    path('message_save_view', discussion_views.message_save_view, name='message_save_view'),
    path('message_delete_view', discussion_views.message_delete_view, name='message_delete_view'),

    path('', include('home.urls')),
    path('', include('friends.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

