from django.db import models

class Category(models.Model):
    ''' Model for the stock categories '''

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        ''' Changes the default object name '''
        return self.name

    def get_display_name(self):
        ''' Function to return the display name '''
        return self.display_name


class Product(models.Model):
    category = models.ForeignKey("Category",
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
