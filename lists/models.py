from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

class List(models.Model):
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)

	def get_absolute_url(self):
		return reverse('view_list', args=[self.id])

	@staticmethod
	def create_new(first_item_text, owner=None):
		list_ = List.objects.create(owner=owner)
		Item.objects.create(text=first_item_text, list=list_)
		return list_

	@property
	def name(self):
		return self.item_set.first().text
		
class Item(models.Model):
	text = models.TextField(default='') 
	# blank=False is default, If a field has blank=True, form validation will 
	# allow entry of an empty value. If a field has blank=False, the field will
	# be required.		
	list = models.ForeignKey(List, default=None)

	def __str__(self):
		return self.text

	class Meta:
		ordering = ('id',)
		unique_together = ('list', 'text')