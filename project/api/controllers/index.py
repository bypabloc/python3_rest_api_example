from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from ..models import Company
import json

@api_view(['GET'])
def findAll(request):
    companies = list(Company.objects.values())

    if len(companies) > 0:
        data = {
            'status': 'success',
            'data': companies,
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
    data = {}

    try:

        body = json.loads(request.body)
        data['body'] = body

        Company.objects.create(
            name=body['name'],
            description=body['description'],
            url=body['url'],
            city=body['city'],
            address=body['address'],
        )

        data['status'] = 'success'
        data['message'] = 'Creado exitosamente'

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
        }
    
    return Response(data)
