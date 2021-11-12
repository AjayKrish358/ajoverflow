from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Questions(models.Model):
    ques_id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    question=models.CharField(max_length=500,unique=True)
    slug=AutoSlugField(('slug'),max_length=500,unique=True,populate_from=('question',))
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return f'{self.question}'

class Answers(models.Model):
    ques_id=models.ForeignKey(Questions,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)#id of the user answering
    answer=models.CharField(max_length=500,unique=True)
    upvote=models.IntegerField(default=0)
    downvote=models.IntegerField(default=0)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
           return f'{self.answer}'



  
    