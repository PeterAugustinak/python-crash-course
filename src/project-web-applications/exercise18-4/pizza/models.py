# 18-4

from django.db import models


# Create your models here.
class Pizza(models.Model):
    """A model for building specific Pizza."""
    pizza_name = models.CharField(max_length=30)

    def __str__(self):
        """Return a string representation of the model."""
        return self.pizza_name


class Topping(models.Model):
    """A model for specific Topping on the specific Pizza."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        """Return a string representation of the model."""
        return self.topping_name

