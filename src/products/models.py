from django.db import models

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=120) # requird
	description =models.TextField(blank=True,null=True) #blank for web, null for database
	price = models.DecimalField(max_digits=1000, decimal_places=2)

	summary = models.TextField(default="This is cool")
	featured = models.BooleanField(default=True)