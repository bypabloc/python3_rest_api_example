from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from ..models import User
from ..validations.user import UserFormCreate

@api_view(['GET'])
def findAll(request):

    users = list(User.objects.values())

    if len(users) > 0:
        data = {
            'status': 'success',
            'data': users,
        }
    else:
        data = {
            'status': 'error',
            'message': 'No hay datos',
        }

    return Response(data)
        
@api_view(['POST'])
@csrf_exempt
def create(request):
    
    user = UserFormCreate(request.POST)

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

    try:
        data = {
            'status': 'success',
        }
    except Exception as ex:
        trace = []
        tb = ex.__traceback__
        while tb is not None:
            trace.append({
                "filename": tb.tb_frame.f_code.co_filename,
                "name": tb.tb_frame.f_code.co_name,
                "lineno": tb.tb_lineno
            })
            tb = tb.tb_next
        
        data = {
            'status': 'error',
            'message': 'No hay datos',
            'trace': trace,
            'body': body,
        }
    