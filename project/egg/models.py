from django.db import models
from django.conf import settings

# Create your models here.

class Egg(models.Model):
    number = models.IntegerField(primary_key=True)
    coin = models.IntegerField(default=0)
    pos = models.CharField(max_length=20, default='0/0')

    def __str__(self):
        return str(self.number) + "&" + str(self.coin) + "&" + self.pos
