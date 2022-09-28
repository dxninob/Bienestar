from django.db import models

# Create your models here.
class Module(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    class Meta:
        db_table = 'modules'

# class Activity(models.Model):
#     description = models.CharField(max_length=255)
#     module = models.ForeignKey(Module, on_delete=models.CASCADE)
#     #user = models.ManyToManyField(User)
#     class Meta:
#         db_table = 'activities'