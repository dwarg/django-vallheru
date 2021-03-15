from django.db import models
from players.models import Player


class Equipment(models.Model):
    name = models.CharField(max_length=255)
    power = models.IntegerField(default=0)
    status = models.CharField(max_length=1)
    eq_type = models.CharField(max_length=15)
    level = models.IntegerField(default=1)
    dexterity = models.IntegerField(default=0)
    endurance = models.IntegerField()
    speed = models.IntegerField(default=0)
    poison = models.IntegerField(default=0)
    max_endurance = models.IntegerField()
    repair = models.IntegerField()
    two_handed = models.BooleanField(default=False)
    cost = models.IntegerField()
    shop = models.BooleanField(default=False)
    magic = models.BooleanField(default=False)
    player = models.ForeignKey(Player, null=True)

    def __str__(self):
        return self.name
