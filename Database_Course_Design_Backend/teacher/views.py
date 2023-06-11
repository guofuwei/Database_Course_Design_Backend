from django.http import JsonResponse


# Create your views here.
def test(request):
    return JsonResponse({"message": "Hello, world!"})
