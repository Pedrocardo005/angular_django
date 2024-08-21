
from django.http import JsonResponse
from new_app.models import ExampleModel


def get_data(request):
    data = ExampleModel.objects.all()
    return JsonResponse(data, safe=False)
