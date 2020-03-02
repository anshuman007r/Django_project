# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from .models import Board,Topic,Post
from django.contrib.auth.models import User
from django.shortcuts import render,get_object_or_404,redirect
from .forms import NewTopicForm

@login_required
def home(request):                                 
    board=Board.objects.all()
    return render(request,'home.html',{'board':board})

@login_required
def board_topic(request,pk):
    board=get_object_or_404(Board,pk=pk)
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
    return render(request,'topic_post.html',{'topic':topic})

@login_required
def edit_post(request,pk,topic_pk):
    topic=get_object_or_404(Topic,boards__pk=pk,pk=topic_pk)
    if request.method=="POST":
       change_subject=request.POST['change_subject']
       change_message=request.POST['change_message']
       topic=Topic.objects.get(pk=topic_pk)
       topic=Topic.objects.filter(pk=topic_pk)
       topic.update(subject=change_subject)

       return redirect('topic_post',pk,topic_pk) 
    return render(request,'edit_post.html',{'topic':topic})

