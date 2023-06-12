from django.http import JsonResponse
from student.models import Student
import json


# Create your views here.
def test(request):
    return JsonResponse({"message": "Hello, world!"})


def make_res(select_res):
    array_res = []
    for i in select_res:
        array_res.append({
            "id": i.id,
            "name": i.name,
            "sex": i.sex,
            "student_id": i.student_id,
            "department": i.department,
            "class_name": i.class_name,
            "telephone": i.telephone
        }
        )
    return array_res


def get_all(request):
    if request.method != "GET":
        return JsonResponse({"code": "400", "msg": "请求方法错误"})
    student = Student.objects.all()
    res = make_res(student)
    return JsonResponse({"code": "200", "data": res})


def get_by_filter(request):
    if request.method != "GET":
        return JsonResponse({"code": "400", "msg": "请求方法错误"})
    # 获取get params
    id = request.GET.get("id")
    name = request.GET.get("name")
    sex = request.GET.get("sex")
    department = request.GET.get("department")
    class_name = request.GET.get("class_name")
    student_id = request.GET.get("student_id")
    telephone = request.GET.get("telephone")
    # 用上述不为空的值构建filter字典
    filter_dict = {}
    if id is not None:
        filter_dict["id"] = id
    if name is not None:
        filter_dict["name"] = name
    if sex is not None:
        filter_dict["sex"] = sex
    if department is not None:
        filter_dict["department"] = department
    if class_name is not None:
        filter_dict["class_name"] = class_name
    if student_id is not None:
        filter_dict["student_id"] = student_id
    if telephone is not None:
        filter_dict["telephone"] = telephone
    # 用filter字典查询
    student = Student.objects.filter(**filter_dict)
    res = make_res(student)
    return JsonResponse({"code": "200", "data": res})


def add(request):
    if request.method != "POST":
        return JsonResponse({"code": "400", "msg": "请求方法错误"})
    # 获取post body
    body = request.body
    # 解析json格式的body

    body = json.loads(body)
    # 获取body中的参数
    name = body.get("name")
    sex = body.get("sex")
    department = body.get("department")
    class_name = body.get("class_name")
    student_id = body.get("student_id")
    telephone = body.get("telephone")
    # 新建学生
    Student.objects.create(name=name, sex=sex, department=department, class_name=class_name, student_id=student_id,
                           telephone=telephone)
    return JsonResponse({"code": "200", "msg": "ok"})
