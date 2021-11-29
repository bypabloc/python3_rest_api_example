from django.urls import path, include

urlpatterns = [
    path('companies/', include('api.routes.companies')),
    path('users/', include('api.routes.users')),
]