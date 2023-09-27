from django.db import models

# Create your models here.


class Shop(models.Model):
    lastupdate = models.DateTimeField(primary_key=True, auto_now_add=True)
    item1 = models.IntegerField(default=0)
    item2 = models.IntegerField(default=0)
    item3 = models.IntegerField(default=0)

    def __str__(self):
        return self.item1 + "&" + self.item2 + "&" + self.item3
