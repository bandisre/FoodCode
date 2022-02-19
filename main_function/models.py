from django.db import models

class Additive_list(models.Model):
    name = models.TextField() #additive name
    description = models.TextField() #additive description

    def __str__(self):
        return self.name
    



# Create your models here.
