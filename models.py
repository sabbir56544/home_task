from django.db import models

class Writer(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField()
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name 


class Publication(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name
