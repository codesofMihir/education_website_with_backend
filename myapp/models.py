from django.db import models

# Create your models here.

class Products(models.Model):
    user=models.ForeignKey('auth.user',on_delete=models.CASCADE)
    product_name=models.CharField(max_length=200)
    description=models.TextField()
    qty=models.IntegerField(default=1)
    product_image=models.ImageField(upload_to='product_images/',blank=True,null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.product_name

