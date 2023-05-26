from django.urls import path
from .views import *
urlpatterns = [
    path("",login,name="login"),
    path("add/",add,name="add"),
    path("update/<int:pk>",update,name="update"),
    path("delete/",delete,name='delete'),
    path("delete_item/<int:pk>",delete_item,name='delete_item'),
    path("product_manager/",product_manager,name='product_manager')

]