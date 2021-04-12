from django.db import models
from datetime import date
from django.contrib.postgres.fields import ArrayField
from json import dumps


class Base:
    def to_json(self):
        return {
            '{}'.format(key): value for key, value in self.__dict__.items()
            if key != '_state'
        }


class Text(Base, models.Model):
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'texts'
        ordering = ['-created_at']


class Entity(Base, models.Model):
    date = ArrayField(
        models.CharField(max_length=128, blank=True)
    )
    text = models.OneToOneField(Text, on_delete=models.CASCADE)
    location = ArrayField(
        models.CharField(max_length=128, blank=True)
    )
    keywords = ArrayField(
        models.CharField(max_length=128, blank=True)
    )
    person = ArrayField(
        models.CharField(max_length=128, blank=True)
    )
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'entities'
        ordering = ['-created_at']


class Sentiment(Base, models.Model):
    text = models.OneToOneField(Text, on_delete=models.CASCADE)
    polarity = models.CharField(max_length=128)
    subjectivity = models.CharField(max_length=128)
    polarity_confidence = models.FloatField()
    subjectivity_confidence = models.FloatField()
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'sentiments'
        ordering = ['-created_at']
