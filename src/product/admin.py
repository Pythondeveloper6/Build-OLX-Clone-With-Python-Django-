from django.contrib import admin

# Register your models here.
from .models import Product , Category , Brand , ProductImages

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProductImages)
