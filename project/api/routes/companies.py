from django.urls import path
from ..controllers.CompanyController import findAll, create

urlpatterns = [
    path('find_all', findAll, name='companies_find_all'),
    path('create', create, name='companies_create'),
]