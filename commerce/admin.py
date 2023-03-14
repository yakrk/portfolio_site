from django.contrib import admin
from .models import Product, ProductCategory, ProductPrice, \
    PurchaseItem, PurchaseHistory, TaxRate, Stock, Cart, CartItem
from django.utils.html import format_html
from django.utils import formats
# Register your models here.


class ProductPriceInline(admin.TabularInline):
    model = ProductPrice
    extra = 1


class StockInline(admin.TabularInline):
    model = Stock
    extra = 1


class ProductAdmin(admin.ModelAdmin):  # adds fields to listview of admin page
    list_display = ("id", "category_name", "product_name",
                    "product_is_published")
    list_display_links = ("id", "product_name")  # allow link
    list_filter = ("category_name", "product_is_published")  # adds filter
    list_per_page = 25  # define max items per page
    list_editable = ("product_is_published", )
    search_fields = ("product_name", "product_description")
    inlines = [
        ProductPriceInline,
        StockInline,
    ]


class ProductPriceAdmin(admin.ModelAdmin):
    list_display = ("id", "standard_price",
                    "discount_price", "is_discount_price_on", "price_with_tax")
    list_display_links = ("id",)


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category_name", )
    list_display_links = ("id",)
    list_per_page = 25
    list_editable = ("category_name",)


class TaxRateAdmin(admin.ModelAdmin):
    list_display = ("id", "tax_rate",)
    list_display_links = ("id",)
    list_editable = ("tax_rate",)


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 3


class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "total_price", "last_update")
    list_display_links = ("id", )
    list_per_page = 25
    inlines = [
        CartItemInline,
    ]


class PurchaseItemInline(admin.TabularInline):
    model = PurchaseItem
    extra = 2

class PurchaseHistoryAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "purchased_date", "total_price")
    list_display_links = ("id", )  # allow link
    list_filter = ("user", )  # adds filter
    list_per_page = 25  # define max items per page
    search_fields = ("user", "product")

    inlines = [
        PurchaseItemInline,
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(TaxRate, TaxRateAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(ProductPrice, ProductPriceAdmin)
admin.site.register(PurchaseHistory, PurchaseHistoryAdmin)
