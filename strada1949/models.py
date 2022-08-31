from django.db import models
import uuid
from cloudinary.models import CloudinaryField

# Create your models here.


class Collection(models.Model):
    collection_name = models.CharField(
        max_length=4,
        verbose_name='Collection Name'
    )
    collection_number = models.CharField(
        max_length=4,
        verbose_name='Collection Number'
    )
    collection_color = models.CharField(
        max_length=7,
        verbose_name='Collection Color (HEX)'
    )
    collection_slug = models.CharField(
        max_length=8,
        verbose_name='Collection Slug (Link)'
    )

    def __str__(self):
        return self.collection_name


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Product Name',
    )

    price = models.CharField(
        max_length=5,
        verbose_name='Price'
    )

    collection = models.ForeignKey(
        Collection,
        on_delete=models.CASCADE
    )

    featured = models.BooleanField(
        verbose_name='Featured'
    )

    # img1 = models.ImageField(
    #     upload_to='media',
    #     verbose_name='Image 1'
    # )

    # img2 = models.ImageField(
    #     upload_to='media',
    #     verbose_name='Image 2'
    # )

    # img3 = models.ImageField(
    #     upload_to='media',
    #     verbose_name='Image 3'
    # )

    img1 = CloudinaryField('image')

    img2 = CloudinaryField('image')
    
    img3 = CloudinaryField('image')

    male = models.BooleanField(
        verbose_name='Male Clothing'
    )

    female = models.BooleanField(
        verbose_name='Female Clothing'
    )

    description = models.CharField(
        max_length=500,
        verbose_name='Product Description'
    )

    product_id = models.CharField(
        max_length=128,
        verbose_name='Product ID',
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        null=False
    )

    product_sku = models.CharField(
        max_length=20,
        verbose_name='Product SKU',
        default='UOsMRnHs'
    )

    def __str__(self):
        return self.name

class Order(models.Model):
    first_name = models.CharField(
        max_length=128,
        verbose_name='First Name',
        null=False
    )

    last_name = models.CharField(
        max_length=128,
        verbose_name='Last Name',
        null=False
    )

    address1 = models.CharField(
        max_length=150,
        verbose_name='Address Line 1',
        null=False
    )

    address2 = models.CharField(
        max_length=150,
        verbose_name='Address Line 2',
        null=False
    )

    city = models.CharField(
        max_length=150,
        verbose_name='City',
        null=False
    )

    state = models.CharField(
        max_length=150,
        verbose_name='State',
        null=False
    )

    zip_code = models.CharField(
        max_length=10,
        verbose_name='ZIP Code',
        null=False
    )

    country = models.CharField(
        max_length=50,
        verbose_name='Country',
        default='India',
        null=False
    )

    email = models.CharField(
        max_length=250,
        verbose_name='Email',
        null=False
    )

    phone = models.CharField(
        max_length=10,
        verbose_name='Phone',
        null=False
    )

    order = models.CharField(
        max_length=10000,
        verbose_name='Order',
        null=False
    )

    order_id = models.UUIDField(
        max_length=128,
        verbose_name='Order ID',
        primary_key=True,
        default=uuid.uuid4,
        null=False
    )

    completed = models.BooleanField(
        verbose_name='Order Completed',
        default=False
    )

    def __str__(self):
        return self.first_name + " " + self.last_name