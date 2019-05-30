from datetime import timedelta

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.datetime_safe import datetime


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    pages = models.CharField(max_length=50)
    publication_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    summary = models.TextField(max_length=100)
    cover = models.ImageField(upload_to='book/cover/', null=True, blank=True)
    reservation = models.BooleanField(null=False, blank=True)

    def __str__(self):
        return self.title + ' - ' + self.author

    def delete(self, *args, **kwargs):
        self.cover.delete()
        super().delete(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, null=True, blank=True)
    cpf = models.IntegerField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    registration_id = models.IntegerField(null=True, blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class ReservationBook(models.Model):
    idbook = models.IntegerField(null=False, blank=True)
    idUser = models.IntegerField(null=False, blank=True)
    # date_now = models.DateField()
    # expireDate = models.DateField(default=datetime.now()+timedelta(days=10))

    def __str__(self):
        return str(self.idbook)


