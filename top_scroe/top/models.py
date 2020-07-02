from django.db import models


# Create your models here.

class Client(models.Model):
    client = models.CharField('客户端', max_length=10,primary_key=True)
    score = models.IntegerField('分数')

    def __str__(self):
        return self.client
