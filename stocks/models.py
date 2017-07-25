from django.db import models

# Create your models here.

class Stock(models.Model):
	stock = models.CharField(max_length=120)

	def __str__(self):
		return self.stock