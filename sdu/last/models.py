from django.db import models


class User(models.Model):
    login = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    firs = models.CharField(max_length=50)
    number = models.IntegerField()
    city = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)

    def __str__(self):
        return self.login
