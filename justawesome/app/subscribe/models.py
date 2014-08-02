from django.db import models

class Subscriber(models.Model):
	email = models.EmailField()

	def __unicode__(self):
		return self.email
