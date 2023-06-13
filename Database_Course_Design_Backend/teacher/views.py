from django.http import JsonResponse
from teacher.models import Teacher
import json
from utils.utils import make_res


# Create your views here.
def test(request):
    return JsonResponse({"message": "Hello, world!"})


def get_all(request):
    if request.method != "GET":
        return JsonResponse({"code": "400", "msg": "请求方法错误"})
    teacher = Teacher.objects.all()
    res = make_res(teacher, "teacher")
    return JsonResponse({"code": "200", "data": res})


def get_by_filter(request):
    if request.method != "GET":
        return JsonResponse({"code": "400", "msg": "请求方法错误"})
    # 获取get params
    this_id = request.GET.get("id")
    name = request.GET.get("name")
    teacher_id = request.GET.get("teacherId")
    course_id = request.GET.get("courseId")
    # 用上述不为空的值构建filter字典
    filter_dict = {}
    if this_id is not None:
        filter_dict["id"] = this_id
    if name is not None:
        filter_dict["name"] = name
    if teacher_id is not None:
        filter_dict["teacher_id"] = teacher_id
    if course_id is not None:
        filter_dict["course_id"] = course_id
    # 用filter字典查询
    teacher = Teacher.objects.filter(**filter_dict)
    res = make_res(teacher, "teacher")
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
    teacher_id = body.get("teacherId")
    course_id = body.get("courseId")
    # 当有参数为空，返回错误
    if body is None or name is None or teacher_id is None or course_id is None:
        return JsonResponse({"code": "401", "msg": "参数错误"})
    # 新建学生
    Teacher.objects.create(name=name, teacher_id=teacher_id, course_id=course_id)
    return JsonResponse({"code": "200", "msg": "ok"})


def delete(request):
    if request.method != "POST":
        return JsonResponse({"code": "400", "msg": "请求方法错误"})
    # 获取post body
    body = request.body
    # 解析json格式的body
    body = json.loads(body)
    # 获取body中的参数
    this_id = body.get("id")
    # 当有参数为空，返回错误
    if body is None or this_id is None:
        return JsonResponse({"code": "401", "msg": "参数错误"})
    # 删除学生
    Teacher.objects.filter(id=this_id).delete()
    return JsonResponse({"code": "200", "msg": "ok"})
