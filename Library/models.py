import email
from email.policy import default
from inspect import modulesbyfile
from pyexpat import model
from unicodedata import name
from django.db import models
from matplotlib.pyplot import title
from datetime import date

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=30)
    # ISPN = models.IntegerField(default=2000)
    author = models.CharField(max_length=30)
    copies = models.IntegerField(default=1)
    # desc = models.TextField()
    bookImg_url = models.URLField()
    ebook_url = models.CharField(default="None",max_length=100)


    def __str__(self):
        return self.title + " " + self.author
# class Book(models.Model):
#     title = models.CharField(max_length=30)
#     # ISPN = models.IntegerField(default=2000)
#     author = models.CharField(max_length=30)
#     copies = models.IntegerField(default=1)
#     # desc = models.TextField()
#     bookImg_url = models.URLField()
#     ebook_url = models.URLField()


#     def __str__(self):
#         return self.title + " " + self.author
class Users(models.Model):
    user_name = models.CharField(max_length=10)
    email = models.EmailField()
    mobile = models.IntegerField()
    user_id = models.IntegerField()
    gender = models.CharField(max_length=6)
    catagory = models.CharField(max_length=60)
    penalty = models.IntegerField()
    duration = models.IntegerField()
    count = models.IntegerField()
    limit = models.IntegerField()
    def __str__(self):
        return self.user_name + " " + self.catagory


# class available_books(models.Model):
#     title = models.CharField(max_length=30)
#     ISBN = models.IntegerField(default=2000,unique=True)
#     def __str__(self):
#         return str(self.title)+'__'+str(self.ISBN)
    
# class book_transaction(models.Model):
#     user_id = models.ForeignKey('users',to_field='user_id',on_delete=models.CASCADE)
#     ISBN = models.IntegerField(default=2000,unique=True)
#     title = models.CharField(max_length=30)
#     issue_date = models.DataField(default=date.today(),null=True)
#     deadline=models.DataField(default=date.today(),ull=True)
#     def __str__(self):
#         return str(self.user_id)+"___"+str(self.title)
    
class Sign(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=15)
    email = models.CharField(max_length=60)
    # password2 = models.CharField(max_length=15)
    def __str__(self):
        return self.username