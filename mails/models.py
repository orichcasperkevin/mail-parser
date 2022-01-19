from django.db import models

# Create your models here.
class Mail(models.Model):
	date = models.DateTimeField()
	source_email = models.CharField(max_length=250,default="None")
	pro_number = models.CharField(max_length=100)
	loaded_miles = models.IntegerField()
	pickup = models.DateTimeField()
	delivery = models.DateTimeField()
	no_of_additional_stops = models.IntegerField()
	vehicle_size = models.CharField(max_length=100)
	commodity = models.CharField(max_length=100)
	max_pieces = models.IntegerField()
	max_weight = models.IntegerField()
	from_address = models.CharField(max_length=250,default="None")
	to_address = models.CharField(max_length=250,default="None")
	dimensions = models.CharField(max_length=20)
	stackable = models.CharField(max_length=20)
