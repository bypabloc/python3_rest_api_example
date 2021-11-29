from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from ..validations.auth import AuthSignUpForm, AuthSignInForm, AuthSignOutForm

@api_view(['POST'])
@csrf_exempt
def signUp(request):
    
    user = AuthSignUpForm(request.POST)

    if user.is_valid():
        user.save()
        data = {
            'data': user.cleaned_data,
        }
        return Response(data, status=status.HTTP_201_CREATED)
    else:
        data = {
            'errors': user.getErrors(),
        }
        return Response(data, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

@api_view(['POST'])
@csrf_exempt
def signIn(request):
    
    user = AuthSignInForm(request.POST)

    if user.is_valid():
        data = {
            'data': user.cleaned_data,
        }
        return Response(data, status=status.HTTP_201_CREATED)
    else:
        data = {
            'errors': user.getErrors(),
        }
        return Response(data, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

@api_view(['POST'])
@csrf_exempt
def signOut(request):
    
    user = AuthSignUpForm(request.POST)

    if user.is_valid():
        user.save()
        data = {
            'data': user.cleaned_data,
        }
        return Response(data, status=status.HTTP_201_CREATED)
    else:
        data = {
            'errors': user.getErrors(),
        }
        return Response(data, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
