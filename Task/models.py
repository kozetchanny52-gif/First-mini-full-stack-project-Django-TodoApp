from turtle import mode
from unicodedata import category

from django.db import models

class Task(models.Model):
    
    categories = {
    "low": "Low",
    "medium": "Medium",
    "high": "High",
}
    types={
            "normal":"Normal",
            "urgent":"Urgent"
    }
    ID=models.BigAutoField(primary_key=True)
    title=models.CharField('Title',max_length=200,unique=True)
    category=models.CharField(max_length=10,choices=categories)
    type=models.CharField(max_length=10,choices=types)
    is_complete=models.BooleanField(default=False)
    Created_At=models.DateTimeField('Is_created_at',auto_now_add=True)
    Updated_At=models.DateTimeField('Updated_At',auto_now=True)
    deadline=models.DateTimeField('Scheduled_at',null=True,blank=True)

    def __str__(self):
        return f"Title: {self.title} , Category: {self.category}, Type: {self.type}"

    