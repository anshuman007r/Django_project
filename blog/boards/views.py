# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from .models import Board,Topic,Post
from django.contrib.auth.models import User
from django.shortcuts import render,get_object_or_404,redirect
from .forms import NewTopicForm
from .forms import ReplyForm

@login_required
def home(request):                                 
    board=Board.objects.all()
    return render(request,'home.html',{'board':board})

@login_required
def board_topic(request,pk):
    board=get_object_or_404(Board,pk=pk)
    post=Post.objects.all()
    return render(request,'topic.html',{'board':board})

@login_required
def new_topic(request,pk):
    board=get_object_or_404(Board,pk=pk)
    form=NewTopicForm()
    if request.method=='POST':
       form=NewTopicForm(request.POST)

       if form.is_valid():
          topic=form.save(commit=False)
          topic.starter=request.user
          topic.boards=board
          topic.save()
          post=Post.objects.create(
          message=form.cleaned_data.get('message'),
          created_by=request.user,
          topic=topic)
          post.save()
       else:
          form=NewTopicForm()
       return redirect('board_topic',pk=board.pk)

    return render(request,'new_topic.html',{'board':board,'form':form})

@login_required
def topic_post(request,pk,topic_pk):
    topic=get_object_or_404(Topic,boards__pk=pk,pk=topic_pk)
    topic.watch+=1
    topic.save()
    return render(request,'topic_post.html',{'topic':topic})

@login_required
def edit_post(request,pk,topic_pk,post_pk):
    post=get_object_or_404(Post,topic__boards__pk=pk,topic__pk=topic_pk,pk=post_pk)    
    if request.method=="POST":
       message=request.POST['message']
       post=Post.objects.filter(pk=post_pk)
       post.update(message=message)  
       return redirect('topic_post',pk=pk,topic_pk=topic_pk)
    return render(request,'edit_post.html',{'post':post})

@login_required
def reply_post(request,pk,topic_pk):
    topic=get_object_or_404(Topic,boards__pk=pk,pk=topic_pk)
    form=ReplyForm()
    if request.method=="POST":
       form=ReplyForm(request.POST)
       if form.is_valid():
            post=form.save(commit=False)
            post.created_by=request.user
            post.topic=topic
            post.save()
       else:
            form=ReplyForm()
       return redirect('topic_post',pk=pk,topic_pk=topic_pk)           
    return render(request,'reply_post.html',{'topic':topic,'form':form})


