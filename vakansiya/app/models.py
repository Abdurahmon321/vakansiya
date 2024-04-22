from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Vakansiya(models.Model):
    name = models.CharField(max_length=100)
    vakansiya_haqida = models.TextField()
    tajriba_talab_qilinadi = models.IntegerField()
    ish_haqida = models.TextField()
    yosh_chegara = models.CharField(max_length=255)
    img = models.ImageField(upload_to="vakansiya/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    vaqti = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    mobile = models.CharField(max_length=13)
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    img = models.ImageField(upload_to="user_profile/")

    def __str__(self):
        return self.firstname


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    vakansiya = models.ForeignKey(Vakansiya, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
