from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField
from django.db.models.fields.related import ManyToManyField

class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(postData['first']) < 2:
            errors["first_name"] = "first name name should be at least 2 characters"
        if len(postData['last']) < 2:
            errors["last_name"] = "last name description should be at least 2 characters"
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if len(postData['passwod']) < 8:
            errors['password'] = "the password should be 8 digits at least"
        if postData['passwod'] != postData['cpw']:
            errors['confirm_password'] = "passwords doesn't match"
        return errors

    def login_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if len(postData['passwod']) < 8:
            errors['password'] = "the password should be 8 digits at least"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255) 
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255) 
    password = models.CharField(max_length=45) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=BlogManager()


class Books(models.Model):

    title=models.CharField(max_length=255)
    desc = models.TextField(max_length=255)
    users = models.ManyToManyField(User, related_name='books')
    uploaded_by_id= models.ForeignKey(User, related_name='user' ,on_delete=CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Authors(models.Model):
    name=models.CharField(max_length=255)
    author = models.ManyToManyField(Books, related_name=('publishers'))
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

def create_user(first_name, last_name, email, password):
    return User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)

def get_user(email,password):
    users=User.objects.filter(email = email, password = password)
    if len(users) > 0 :
        return users[0]
    return None

def registration_validation(post_data):
    return User.objects.basic_validator(post_data)

def login_validator(post_data):
    return User.objects.login_validator(post_data)

# def create_book(title,desc,user_id):
#     user = User.objects.get(id=user_id)
#     new_book=Books.objects.create(title=title,desc=desc, uploaded_by_id = user_id)
#     user.books.add(new_book)
#     return new_book

# def getfavbooks(user_id):
#     user = User.objects.get(id=user_id)
#     return user.books.all()

# def create_author(name):
#     new_author=Authors.objects.create(name=name)
#     return new_author
# def allbooks():
#     return Books.objects.all()
# def getBook(id):
#     return Books.objects.get(id=id)
# def getAuthor(id):
#     return Authors.objects.get(id=id)
# def allAuthors():
#     return Authors.objects.all()
# def add_fav_book(book_id,user_id):
#     user = User.objects.get(id=user_id)
#     book = Books.objects.get(id = book_id)
#     user.books.add(book)
