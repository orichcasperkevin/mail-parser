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

class Settings(models.Model):
	user = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	imap_url = models.CharField(max_length=200)
	from_mail = models.CharField(max_length=200)

	def save(self, *args, **kwargs):
		if not self.pk and Settings.objects.exists():
			# if you'll not check for self.pk
			# then error will also raised in update of exists model
			raise ValidationError('There is can be only one Settings instance')
		return super(JuicerBaseSettings, self).save(*args, **kwargs)

class Refresh(models.Model):
	last_refresh = models.DateTimeField()
	def save(self, *args, **kwargs):
		if not self.pk and Refresh.objects.exists():
			# if you'll not check for self.pk
			# then error will also raised in update of exists model
			raise ValidationError('There is can be only one Refresh instance')
		return super(Refresh, self).save(*args, **kwargs)
