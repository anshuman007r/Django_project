"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from boards import views
from accounts import views as account_view
from django.contrib.auth import views as auth_view
urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^signup/$',account_view.signup,name='signup'),
    url(r'^logout/$',auth_view.LogoutView.as_view(),name='logout'),
    url(r'^login/$',auth_view.LoginView.as_view(template_name='login.html'),name='login'),
    url(r'^boards/(?P<pk>\d+)/$',views.board_topic,name='board_topic'),
    url(r'^boards/(?P<pk>\d+)/new/$',views.new_topic,name='new_topic'),
    url(r'^admin/', admin.site.urls),
    url(r'^boards/(?P<pk>\d+)/topic/(?P<topic_pk>\d+)/$',views.topic_post,name='topic_post'),
    url(r'^boards/(?P<pk>\d+)/topic/(?P<topic_pk>\d+)/reply/$',views.reply_post,name='reply_post'),
    url(r'^boards/(?P<pk>\d+)/topic/(?P<topic_pk>\d+)/post/(?P<post_pk>\d+)/$',views.edit_post,name='edit_post'),
]
