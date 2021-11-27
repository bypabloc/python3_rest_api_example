from django.urls import path
from ..controllers.index import snippet_list

urlpatterns = [
    path('', snippet_list, name='companies_list'),
]