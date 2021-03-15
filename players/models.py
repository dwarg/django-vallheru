# -*- encoding: utf-8 -*-

from decimal import Decimal

from django.core.validators import validate_comma_separated_integer_list
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver


class PlayerReligion(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class PlayerRace(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    strength = models.DecimalField(max_digits=5, decimal_places=3, default=Decimal(2.00))
    max_strength = models.DecimalField(max_digits=5, decimal_places=3, max_length=60, default=Decimal(40.00))
    dexterity = models.DecimalField(max_digits=5, decimal_places=3, default=Decimal(2.00))
    max_dexterity = models.DecimalField(max_digits=5, decimal_places=3, max_length=60, default=Decimal(40.00))
    inteligence = models.DecimalField(max_digits=5, decimal_places=3, default=Decimal(2.00))
    max_inteligence = models.DecimalField(max_digits=5, decimal_places=3, max_length=60, default=Decimal(40.00))
    willpower = models.DecimalField(max_digits=5, decimal_places=3, default=Decimal(2.00))
    max_willpower = models.DecimalField(max_digits=5, decimal_places=3, max_length=60, default=Decimal(40.00))
    speed = models.DecimalField(max_digits=5, decimal_places=3, default=Decimal(2.00))
    max_speed = models.DecimalField(max_digits=5, decimal_places=3, max_length=60, default=Decimal(40.00))
    endurance = models.DecimalField(max_digits=5, decimal_places=3, default=Decimal(2.00))
    max_endurance = models.DecimalField(max_digits=5, decimal_places=3, max_length=60, default=Decimal(40.00))
    hp = models.DecimalField(max_digits=5, decimal_places=3, default=Decimal(2.00))  # punkty życia za każdy zdobyty poziom cechy Kondycja

    def __str__(self):
        return self.name


class PlayerClass(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class PlayerManager(UserManager):
    """
    Custom User Model manager.
    It overrides default User Model manager's create_user() and create_superuser,
    which requires username field.
    """

    def create_user(self, email, password=None, **kwargs):
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.model(email=email, is_staff=True, is_superuser=True, **kwargs)
        user.set_password(password)
        user.save()
        return user


class Player(AbstractBaseUser, PermissionsMixin):
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(_('email address'), blank=False, unique=True)
    first_name = models.CharField(_('first name'), max_length=20)
    last_name = models.CharField(_('last name'), max_length=20)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    level = models.IntegerField(default=1)
    exp = models.IntegerField(default=0)
    energy = models.IntegerField(default=25)
    max_energy = models.IntegerField(default=70)
    hp = models.IntegerField(default=15)
    max_hp = models.IntegerField(default=15)
    ap = models.IntegerField(default=5)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    last_killed = models.DateTimeField(null=True, blank=True)
    last_killed_by = models.ForeignKey('Player', related_name='last_kills', null=True)
    logins = models.IntegerField(default=0)
    race = models.ForeignKey(PlayerRace, null=True)
    player_class = models.ForeignKey(PlayerClass, null=True)
    religion = models.ForeignKey(PlayerReligion, null=True)
    sex = models.CharField(default='man', max_length=10)
    coins = models.IntegerField(default=1000)
    bank_coins = models.IntegerField(default=0)
    strength = models.DecimalField(max_digits=7, decimal_places=3, default=Decimal(0.01))
    dexterity = models.DecimalField(max_digits=7, decimal_places=3, default=Decimal(0.01))
    inteligence = models.DecimalField(max_digits=7, decimal_places=3, default=Decimal(0.01))
    willpower = models.DecimalField(max_digits=7, decimal_places=3, default=Decimal(0.01))
    speed = models.DecimalField(max_digits=7, decimal_places=3, default=Decimal(0.01))
    endurance = models.DecimalField(max_digits=7, decimal_places=3, default=Decimal(0.01))
    magic_points = models.IntegerField(default=3)
    max_magic_points = models.IntegerField(default=6)
    religion_points = models.IntegerField(default=0)

    objects = PlayerManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        unique_together = ("first_name", "last_name")
        verbose_name = _('player')
        verbose_name_plural = _('players')
        abstract = False

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def __str__(self):
        return self.email


class PlayerSkills(models.Model):
    blacksmithing = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal(0.01))
    alchemy = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal(0.01))
    carpentry = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal(0.01))
    wood_working = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal(0.01))
    archery = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal(0.01))
    evasion = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal(0.01))
    mining = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal(0.01))
    herbalism = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal(0.01))
    jewellery = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal(0.01))
    metallurgy = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal(0.01))
    spell_casting = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal(0.01))
    leadership = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal(0.01))
    breeding = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal(0.01))
    melee = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal(0.01))
    perceptivity = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal(0.02))
    player = models.OneToOneField(Player, related_name="skills")


@receiver(post_save, sender=Player)
def create_favorites(sender, instance, created, **kwargs):
    if created:
        PlayerSkills.objects.create(player=instance)
