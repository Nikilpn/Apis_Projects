from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    name=models.CharField(max_length=100)
    user_object=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    status=models.BooleanField(default=False)

    assigned_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


