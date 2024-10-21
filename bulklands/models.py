from django.db import models

class Agent(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    whatsapp_number = models.CharField(max_length=15)
    email = models.EmailField()
    property_type = models.CharField(max_length=50, choices=[('buy', 'Buy Property'), ('sell', 'Sell Property')])
    property_category = models.CharField(max_length=50, choices=[
        ('agriculture', 'Agriculture'), 
        ('layouts', 'Layouts'),
        ('industrial', 'Industrial'),
        ('commercial', 'Commercial'),
        ('residential', 'Residential'),
    ])
    location = models.CharField(max_length=250)
    square_yards = models.CharField(max_length=50)
    budget_range = models.CharField(max_length=50)

    def __str__(self):
        return self.name
