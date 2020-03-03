# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
      name=models.CharField(max_length=30,unique=True)
      description=models.CharField(max_length=40)
      def __str__(self):
          return self.name
      def get_post_count(self):
          self.count=0
          for post in Post.objects.all():
              if self.pk==post.topic.boards.pk:
                 self.count+=1
          return self.count
      def get_last_update(self):
          last=Post.objects.get(pk=self.count)
          self.last=last.updated_at
          return self.last

class Topic(models.Model):
      subject=models.CharField(max_length=50)
      last_updated=models.DateTimeField(auto_now_add=True)
      boards=models.ForeignKey(Board,on_delete=models.CASCADE,related_name='topic')
      starter=models.ForeignKey(User,on_delete=models.CASCADE,related_name='topic')
      watch=models.IntegerField(default=0)
      def __str__(self):
          return self.subject

class Post(models.Model):
      message=models.CharField(max_length=255)
      topic=models.ForeignKey(Topic,on_delete=models.CASCADE,related_name='post')
      created_by=models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='post')
      updated_at=models.DateTimeField(auto_now_add=True)
      created_at=models.DateTimeField(null=True)
      updated_by=models.ForeignKey(User,null=True,on_delete=models.CASCADE,related_name='+')
      def __str__(self):
          return self.message

