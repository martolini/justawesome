from django.db import models
from justawesome.core.champion.models import Champion

class Provider(models.Model):
	url = models.URLField(blank=True, null=True)
	name = models.CharField(max_length=100, blank=True, null=True)

	def __unicode__(self):
		return self.name

class Author(models.Model):
	url = models.URLField(blank=True, null=True)
	name = models.CharField(max_length=100, blank=True)

	def __unicode__(self):
		return self.name


class League(models.Model):
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name
	

class Article(models.Model):
	title = models.TextField(blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	nominee = models.ForeignKey(Champion, blank=True, null=True, related_name='nominated_articles')
	provider = models.ForeignKey(Provider, related_name='articles', blank=True, null=True)
	author = models.ForeignKey(Author, related_name='articles', blank=True, null=True)
	league = models.ForeignKey(League, related_name='articles', blank=True, null=True)
	url = models.URLField()
	html = models.TextField(blank=True, null=True)

	def __unicode__(self):
		return self.url

	