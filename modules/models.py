from django.db import models

# Create your models here.
class Module(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    class Meta:
        db_table = 'modules'