from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(unique=True, max_length=11)


class Coordinates(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()


class Level(models.Model):
    winter = models.TextField()
    spring = models.TextField()
    summer = models.TextField()
    autumn = models.TextField()


class Mountain(models.Model):
    NEW = 'NEW'
    PEN = 'PEN'
    ACC = 'ACC'
    REJ = 'REJ'

    STATUS = [
        (NEW, 'new'),
        (PEN, 'pending'),
        (ACC, 'accepted'),
        (REJ, 'rejected'),
    ]


    beauty_title = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255)
    other_title = models.CharField(max_length=255, blank=True)
    connect = models.CharField(max_length=255, blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coord= models.ForeignKey(Coordinates, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=STATUS, default=NEW)


class PerevalImages(models.Model):
    mountain = models.ForeignKey(Mountain, on_delete=models.CASCADE, related_name='images')
    data = models.URLField()
    title = models.CharField(max_length=255)
