from django.http import JsonResponse
from django_q.tasks import async_task

def index(request):
        json_payload = {
            "text": "Hi there"
        }
        async_task("async_django.services.sleep_n_print", 10)
        return JsonResponse(json_payload)