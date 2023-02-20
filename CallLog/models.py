from django.db import models


# Create your models here.
class Log(models.Model):
    from_no = models.CharField(max_length=10)
    to_no = models.CharField(max_length=10)
    start_time = models.DateTimeField(auto_now=True)
