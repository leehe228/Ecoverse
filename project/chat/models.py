from django.db import models

# Create your models here.

class Chat(models.Model):
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=100)
    regtime = models.DateTimeField(primary_key=True, auto_now_add=True)

    def __str__(self):
        return self.name + "&" + self.text
