from django.urls import path
from ..controllers.AuthController import signUp, signIn, signOut

urlpatterns = [
    path('sign_up', signUp, name='auth_sign_up'),
    path('sign_in', signIn, name='auth_sign_in'),
    path('sign_out', signOut, name='auth_sign_out'),
]