from django.db import models

# Create your models here.

class Exchange(models.Model):
    regtime = models.DateTimeField(auto_now_add=True, primary_key=True)
    item_code = models.CharField(max_length=10)
    price = models.IntegerField(default=0)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.item_code + "&" + str(self.price) + "&" + self.name
