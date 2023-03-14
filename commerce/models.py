from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class ProductCategory(models.Model):
    category_name = models.CharField(max_length=200)
    category_description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return str(self.category_name)


class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    category_name = models.ForeignKey(ProductCategory, on_delete=models.DO_NOTHING)
    product_description_short = models.TextField(blank=True, null=True)
    product_description = models.TextField(blank=True, null=True)
    product_is_published = models.BooleanField(default=False)
    product_image = models.ImageField(
        upload_to="product_image/%Y/%m/%d/",
        default=r"noimage.jpg",
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return str(self.product_name)


class TaxRate(models.Model):
    tax_rate = models.DecimalField(max_digits=2, decimal_places=2)

    def __str__(self) -> str:
        return str(self.tax_rate)


class ProductPrice(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, default=0)
    standard_price = models.DecimalField(max_digits=8, decimal_places=0)
    discount_price = models.DecimalField(
        blank=True, null=True, max_digits=8, decimal_places=0
    )
    is_discount_price_on = models.BooleanField(default=False)
    price_with_tax = models.DecimalField(
        max_digits=8, decimal_places=0, editable=False, null=True
    )

    def __str__(self) -> str:
        return str(self.product) + ":  JPY(w/tax) " + str(self.price_with_tax)

    def save(self, *args, **kwargs):
        tax_rate = TaxRate.objects.first().tax_rate
        if self.is_discount_price_on:
            self.price_with_tax = self.discount_price * (1 + tax_rate)
        else:
            self.price_with_tax = self.standard_price * (1 + tax_rate)
        super().save(*args, **kwargs)


class Stock(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    remaining_stock = models.PositiveIntegerField(
        default=0,
    )

    def __str__(self) -> str:
        return str(self.remaining_stock)


# Cart


class Cart(models.Model):
    # id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_price = models.IntegerField(default=0)
    last_update = models.DateTimeField(default=datetime.now())

    def save(self, *args, **kwargs):
        cart_items = CartItem.objects.filter(cart_id=self.id)
        self.total_price = sum([item.cart_item_price for item in cart_items])
        super().save(*args, **kwargs)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    price_with_tax = models.DecimalField(max_digits=8, decimal_places=0, default=0)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    cart_item_price = models.DecimalField(
        max_digits=8, decimal_places=0, default=0, editable=False
    )

    def save(self, *args, **kwargs):
        price = ProductPrice.objects.get(product=self.product)
        self.cart_item_price = self.amount * price.price_with_tax
        super().save(*args, **kwargs)
        # Cart.save(*args, **kwargs)


# Purchase History


class PurchaseHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchased_date = models.DateField(default=None)
    # sent_address = models.TextField(default=None, null=True) #removing temp. TODO Shipping information (address, shipping status, etc.)
    total_price = models.DecimalField(default=0, max_digits=8, decimal_places=0)


class PurchaseItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase_id = models.ForeignKey(PurchaseHistory, on_delete=models.CASCADE)
    amount = models.IntegerField()
    purchased_price = models.DecimalField(max_digits=8, decimal_places=0)
    subtotal = models.DecimalField(max_digits=8, decimal_places=0, default=0)
