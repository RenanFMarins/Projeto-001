from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=65)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Municipality(models.Model):
    name = models.CharField(max_length=65)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Neighborhood(models.Model):
    name = models.CharField(max_length=65)
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Coworking(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    description_is_html = models.BooleanField(default=False)
    property_size = models.IntegerField()
    equipment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='coworkings/covers/%Y/%m/%d/',
                              blank=True, default='')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True,
        default=None,
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    municipality = models.ForeignKey(Municipality, on_delete=models.SET_NULL, null=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
