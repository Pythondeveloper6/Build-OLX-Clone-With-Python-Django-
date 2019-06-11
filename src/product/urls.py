from django.urls import path
from . import views


app_name = 'product'

urlpatterns = [
    path('' , views.productlist , name='product_list') , 
    path('<slug:category_slug>' , views.productlist , name='product_list_category') , 
    path('detail/<slug:product_slug>' , views.productdetail , name='product_detail')
]