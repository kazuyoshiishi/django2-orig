from __future__ import unicode_literals

from django.db import models



# Create your models here.
class Todo(models.Model):
    """todo"""
    name = models.CharField('name', max_length=255)
    detail = models.CharField('detail', max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add = True, verbose_name= 'DATE',)
    memo = models.TextField(null=True)
    DONE = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    dones = models.CharField(max_length=1, choices=DONE)
    
    
    def __str__(self):
        return self.name













