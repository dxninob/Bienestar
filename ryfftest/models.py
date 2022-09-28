from django.db import models
from modules.models import Module

# Create your models here.
class Question(models.Model):
    description = models.CharField(max_length=255)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    class Meta:
        db_table = 'questions'