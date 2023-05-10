from django.db import models

class TypesOfStatus(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.DateField(auto_now=True)


class TypesOfNews(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.AutoField(primary_key=True)


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,
                            null=False,
                            unique=True)
    subname = models.CharField(max_length=20,
                            null=False,
                            unique=True)
    status = models.ForeignKey(TypesOfStatus, on_delete=models.SET_NULL, null=True)


class News(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,
                            null=False,
                            unique=True)
    text = models.TextField(max_length=2500,
                            null=False,
                            unique=True)
    date = models.DateField(auto_now=True)
    authorId = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
    type.id = models.ForeignKey(TypesOfNews, on_delete=models.SET_NULL, null=True)