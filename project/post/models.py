from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=100)
    regtime = models.DateTimeField(primary_key=True, auto_now_add=True)

    def __str__(self):
        return self.name + "&" + self.text

#

