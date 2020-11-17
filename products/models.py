from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):

	title = models.CharField(max_length=225)
	pub_date = models.DateTimeField()
	body = models.TextField()
	url = models.TextField()
	image = models.ImageField(upload_to='image')
	icon = models.ImageField(upload_to='image')
	votes_total = models.IntegerField(default=1)
	hunter = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def summary(self):
		return self.body[:100]

	def date_only(self):
		return self.pub_date.strftime('%b %e %Y') 
