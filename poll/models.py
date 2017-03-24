from django.db import models



class Item(models.Model):
	name = models.CharField(max_length=100)
	itemType = models.CharField(max_length=100)
	itemimage = models.FileField(default='/abcd.jpg')

	def __str__(self):
		content = "ITEM_NAME : " + self.name + "\tITEM_TYPE : " + self.itemType
		return content
	
	

