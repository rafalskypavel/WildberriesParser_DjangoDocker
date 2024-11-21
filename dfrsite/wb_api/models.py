from django.db import models

class Product(models.Model):
    product_id = models.IntegerField()
    brand = models.CharField(max_length=255)
    brand_id = models.IntegerField()
    name = models.CharField(max_length=255)
    entity = models.CharField(max_length=255)
    supplier = models.CharField(max_length=255)
    supplier_id = models.IntegerField()
    supplier_rating = models.FloatField()
    price_u = models.IntegerField()
    sale_price_u = models.IntegerField()
    sale = models.IntegerField()
    rating = models.FloatField()
    review_rating = models.FloatField()
    feedbacks = models.IntegerField()
    total_quantity = models.IntegerField()
