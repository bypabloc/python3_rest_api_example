from django.urls import path, include
from .views import findAll

urlpatterns = [
    path('companies/', findAll.as_view(), name='companies_list'),
    # path('<int:pk>/', CompanyView.as_view()),
]