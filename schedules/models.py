from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.core.exceptions import ValidationError
# Create your models here.

class Schedule(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    name = models.CharField(blank=True, max_length=20)
    
    def __str__(self):
        return "%s - %s" % (self.created_at.date(), self.name)
    

class Activity(models.Model):
    name = models.CharField(blank=False,null=False,max_length=20)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    rank = models.IntegerField(
                    default=1,
                    validators=[MaxValueValidator(5), MinValueValidator(1)]
                 )
    start = models.TimeField()
    end = models.TimeField()
    
    def clean(self,*args,**kwargs):
        if self.start>=self.end:
            raise ValidationError(
                ('start-time: %(start)s must be less than end-time: %(end)s'),
                params={'start': self.start, 'end':self.end},
            )

    def __str__(self):
        return "%s - %s:%s" % (self.name, self.start, self.end)
        
