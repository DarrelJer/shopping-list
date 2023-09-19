from django.urls import path
from main.views import show_main, create_product, show_xml , show_json


app_name = 'main'

urlpatterns = [
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
   
]