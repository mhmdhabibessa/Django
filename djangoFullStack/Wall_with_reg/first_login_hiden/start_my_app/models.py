from django.db import models
from django.db.models.base import Model
from django.db.models.fields import DateTimeField
from django.db.models.fields.related import ManyToManyField

class BlogManager(models.Manager):
    def validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['first_name']) < 2:
            errors["first_name"] = " firsr_name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = " last_name should be at least 2 characters"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    email = models.CharField(max_length=45,default=True)
    confm_password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)      
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)