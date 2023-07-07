from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True,primary_key=True)
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Todo(models.Model):
    id=models.CharField(max_length=50, primary_key=True)
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    due_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=(
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ))


class TodoShare(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    shared_with = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    access_level = models.CharField(max_length=20, choices=(
        ('read_only', 'Read Only'),
        ('read_write', 'Read/Write'),
        ('approval_required', 'Approval Required'),
    ))


class TodoAccessLog(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    action = models.CharField(max_length=20, choices=(
        ('created', 'Created'),
        ('updated', 'Updated'),
        ('deleted', 'Deleted'),
        ('shared', 'Shared'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ))
    timestamp = models.DateTimeField(auto_now_add=True)
