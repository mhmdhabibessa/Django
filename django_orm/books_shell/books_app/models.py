from django.db import models

class Books(models.Model):
    titel = models.CharField(max_length=255)
    desc= models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Authors(models.Model):
    first_name = models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    nots= models.CharField(max_length=255)
    author= models.ManyToManyField(Books, related_name="publishers",default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    