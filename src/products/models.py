from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
# Create your models here.

class Product(models.Model):
	title = models.CharField(max_length=30) #owiuerpoajsdlfkjasd;flkiu1p3o4u134123 ewjfa;sd
	slug = models.SlugField() # unique=True ,it is a slug field if you want to know more than http://stackoverflow.com/questions/427102/what-is-a-slug-in-django
	description = models.TextField()
	price = models.DecimalField(max_digits=100, decimal_places=2, default=9.99, null=True,) #100.00
	sale_price = models.DecimalField(max_digits=100,
			 decimal_places=2, default=6.99, null=True, blank=True) #100.00

	def __unicode__(self): #in python 3 you have to use __str__ instead of __unicode__
		return self.title


#signals are important for model if you want to know then 
#https://docs.djangoproject.com/en/1.9/ref/signals/#django.db.models.signals.pre_save
def product_pre_save_reciever(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify(instance.title)


pre_save.connect(product_pre_save_reciever, sender=Product)




# def product_post_save_reciever(sender, instance, *args, **kwargs):
# 	if instance.slug != slugify(instance.title):
# 		instance.slug = slugify(instance.title)
# 		instance.save()

# post_save.connect(product_post_save_reciever, sender=Product)