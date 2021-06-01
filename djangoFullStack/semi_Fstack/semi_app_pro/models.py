from django.db import models


class BlogManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = " the titel should be more 2 characters"
        if len(postData['discripton']) < 10:
            errors["discripton"] = "Blog description should be at more 5characters"
        if len(postData['networke']) < 5:
            errors["networke"] = " the networke should be at least 10 characters"
        return errors
    
class TVshown(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    discripton =models.CharField(max_length=255)
    relaied_time= models.DateField(auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()
