# encoding: utf-8
from django.db import models

# Create your models here.
class Question(models.Model):
 question_text=models.CharField('投票问题',max_length=200)
 pub_date = models.DateTimeField('发布日期')
 def __str__(self):
  return self.question_text
 def __unicode__(self):
  return self.question_text
class Choice(models.Model):
 question = models.ForeignKey(Question)
 choice_text = models.CharField('选项',max_length=200)
 votes = models.IntegerField('票数',default=0)
 def __str__(self):
  return self.choice_text
 def __unicode__(self):
  return self.choice_text