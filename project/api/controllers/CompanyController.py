from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from ..models import Company
from ..validations.company import CompanyFormCreate

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
    
    company = CompanyFormCreate(request.POST)

    if company.is_valid():
        company.save()
        data = {
            'data': company.cleaned_data,
        }
        return Response(data, status=status.HTTP_201_CREATED)
    else:
        data = {
            'errors': company.getErrors(),
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
    