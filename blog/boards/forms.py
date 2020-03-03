from django import forms
from .models import Topic,Post

class NewTopicForm(forms.ModelForm):
      message=forms.CharField(widget=forms.Textarea(attrs={'rows':5,'placeholder':"What in you mind?"}),max_length=4000)
      class Meta:
        model=Topic
        fields=['subject','message']

class ReplyForm(forms.ModelForm):
      message=forms.CharField(widget=forms.Textarea(attrs={'rows':5,'placehoder':"Reply to this post"}),max_length=4000)
      class Meta:
         model=Post
         fields=['message']
