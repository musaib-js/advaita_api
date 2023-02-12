from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length = 150)
    subject  = models.CharField(max_length = 200)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Sponsorship(models.Model):
    email = models.EmailField(max_length = 200)
    company_name = models.CharField(max_length = 200)
    contact_person = models.CharField(max_length = 200)
    designation = models.CharField(max_length = 200)
    proposal = models.TextField()

    def __str__(self):
        return self.company_name