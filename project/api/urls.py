from django.urls import path, include
from .views import CompanyView

urlpatterns = [
    path('companies/', CompanyView.as_view(), name='companies_list'),
    # path('<int:pk>/', CompanyView.as_view()),
]