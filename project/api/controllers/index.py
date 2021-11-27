from django.http.response import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from ..models import Company
import json


@api_view(['GET', 'POST'])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        companies = list(Company.objects.values())

        if len(companies) > 0:
            datos = {
                'status': 'success',
                'data': companies,
            }
        else:
            datos = {
                'status': 'error',
                'message': 'No hay datos',
            }

        return JsonResponse(datos)

    elif request.method == 'POST':
        datos = {}

        try:

            body = json.loads(request.body)
            datos['body'] = body

            Company.objects.create(
                name=body['name'],
                description=body['description'],
                url=body['url'],
                city=body['city'],
                address=body['address'],
            )

            datos['status'] = 'success'
            datos['message'] = 'Creado exitosamente'

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
            
            datos = {
                'status': 'error',
                'message': 'No hay datos',
                'trace': trace,
            }
        
        return JsonResponse(datos)

class CompanyView(View):

    @api_view(['GET', 'POST'])
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        companies = list(Company.objects.values())

        if len(companies) > 0:
            datos = {
                'status': 'success',
                'data': companies,
            }
        else:
            datos = {
                'status': 'error',
                'message': 'No hay datos',
            }

        return JsonResponse(datos)

    def post(self, request):

        # body = request.body.decode('utf-8')
        # body = eval(body)
        datos = {}

        try:

            body = json.loads(request.body)
            datos['body'] = body

            Company.objects.create(
                name=body['name'],
                description=body['description'],
                url=body['url'],
                city=body['city'],
                address=body['address'],
            )

            datos['status'] = 'success'
            datos['message'] = 'Creado exitosamente'

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
            
            datos = {
                'status': 'error',
                'message': 'No hay datos',
                'trace': trace,
            }
        
        return JsonResponse(datos)

    def put(self, request):
        return "Update a company"

    def delete(self, request):
        return "Delete a company"