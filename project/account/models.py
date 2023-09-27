from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=50, default='')
    password = models.CharField(max_length=30, default='')
    name = models.CharField(primary_key=True, max_length=30)
    player = models.IntegerField(default=0)

    mission_state = models.IntegerField(default=0)
    submission_state = models.CharField(max_length=10, default='0')
    museum_unlock = models.IntegerField(default=0)
    
    soil_item_unlock = models.IntegerField(default=0)
    energy_item_unlock = models.IntegerField(default=0)

    coin = models.IntegerField(default=0)

    furniture_state = models.CharField(max_length=20, default='000000000000000000')

    smartfarm_state = models.CharField(max_length=50, default='0?0?2021-01-01 00:00:00?0?2021-01-01 00:00:00')

    inventory_state = models.CharField(max_length=200, default='0')

    ecomileage = models.IntegerField(default=0)

    badge_state = models.CharField(max_length=8, default='0000000')

    badge_subinfo = models.CharField(max_length=10, default='0/0/000')

    character_unlock = models.CharField(max_length=10, default='000000')

    def __str__(self):
        return self.email + "&" + self.name + "&" + str(self.player) + "&" + str(self.mission_state) + "&" + self.submission_state + "&" + str(self.museum_unlock) + "&" + str(self.soil_item_unlock) + "&" + str(self.energy_item_unlock) + "&" + str(self.coin) + "&" + self.furniture_state + "&" + self.smartfarm_state + "&" + self.inventory_state + "&" + str(self.ecomileage) + "&" + self.badge_state + "&" + self.badge_subinfo + "&" + self.character_unlock


class Ingame(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    player = models.IntegerField(default=0)
    posx = models.CharField(max_length=5)
    posy = models.CharField(max_length=5)
    posz = models.CharField(max_length=5, default=0)
    rotx = models.CharField(max_length=5, default=0)
    roty = models.CharField(max_length=5, default=0)
    rotz = models.CharField(max_length=5, default=0)

    def __str__(self):
        return self.name + "&" + str(self.posx) + "&" + str(self.posy) + "&" + str(self.posz) + "&" + str(self.rotx) + "&" + str(self.roty) + "&" + str(self.rotz) + "&" + str(self.player)
#
