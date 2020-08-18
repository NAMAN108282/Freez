from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles



class Menu(models.Model):
	Menu_ID = models.CharField(primary_key=True, blank=False, max_length=20)


class MenuItem(models.Model):
	Menu_ID = models.ForeignKey(Menu, on_delete=models.CASCADE)
	Food_Code = models.CharField(max_length=20, primary_key=True, blank=False)
	Food_Name = models.CharField(max_length=50, blank=True, default='NULL')
	VegNveg = models.CharField(default='Veg', max_length=10)
	category = models.CharField(max_length=50, blank=True, default='NULL')
	item_price = models.CharField(max_length=10, default=10.00)
	special_item = models.BooleanField(default=False)
	description = models.CharField(max_length=250, blank=True, default='NULL')
	Meal_Time = models.CharField(max_length=40, blank=True, default='NULL')
	Rating = models.CharField(max_length=30, blank=True, default='NULL')
	Preparation_Time = models.IntegerField(blank=True)

	def __str__(self):
		return self.Food_Code + ":" + self.Food_Name

	class Meta:
		ordering = ['Food_Code']