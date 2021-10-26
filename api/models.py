from django.db import models

# Create your models here.

class Contact(models.Model): 
    first_name = models.TextField(null=True, blank=True)
    last_name = models.TextField(null=True, blank=True)
    email = models.TextField(null=True, blank=True)
    gender = models.TextField(null=True, blank=True)
    phone_number = models.TextField(null=True, blank=True)

    # def __str__(self):
    #     return self.name[0:50]