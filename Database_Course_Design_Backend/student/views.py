from django.http import JsonResponse
from student.models import Student


# Create your views here.
def test(request):
    return JsonResponse({"message": "Hello, world!"})


def get_all(request):
    student = Student.objects.all()
    print(student)
    return JsonResponse({"message": "get_all"})
