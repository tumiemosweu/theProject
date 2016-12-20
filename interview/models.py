from django.db import models
from django.db.models.deletion import CASCADE
from django.template.defaultfilters import default
from django.utils import timezone
import datetime

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30) 
    last_name = models.CharField(max_length=30)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        
    def __str__(self):
        return self.question_text
    
    
class Answer(models.Model):
    BOOLEAN_CHOICES = (
        ('T', 'TRUE'), 
        ('F', 'FALSE'),
        )
    question = models.ForeignKey(Question, on_delete=CASCADE)
    answer_text = models.CharField(max_length=1)
    points_value = models.IntegerField(default= 0)
    
    def __str__(self):
        return self.answer_text
    
class Score(models.Model):
    points = models.ForeignKey(Answer, on_delete=CASCADE)
    score_value = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.score_value
    
    
