from django.http import JsonResponse
from course.models import Course, RC
import json
from utils.utils import make_res
# 引入数据库原子操作
from django.db import transaction


# Create your views here.
def test(request):
    return JsonResponse({"message": "Hello, world!"})


def get_all(request):
    if request.method != "GET":
        return JsonResponse({"code": "400", "msg": "请求方法错误"})
    course = Course.objects.all()
    res = make_res(course, "course")
    for i in res:
        course_id = i.get("id")
        i["resourceIds"] = list(RC.objects.filter(course_id=course_id).values_list("resource_id", flat=True))
    return JsonResponse({"code": "200", "data": res})


def add(request):
    if request.method != "POST":
        return JsonResponse({"code": "400", "msg": "请求方法错误"})
    # 获取post body
    body = request.body
    # 解析json格式的body
    body = json.loads(body)
    # 获取body中的参数
    course_name = body.get("courseName")
    max_select_num = body.get("maxSelectNum")
    resource_ids = body.get("resourceIds")
    # 当有参数为空，返回错误
    if body is None or max_select_num is None or resource_ids is None:
        return JsonResponse({"code": "401", "msg": "参数错误"})

    # 事务
    # noinspection PyBroadException
    try:
        with transaction.atomic():
            # 新建课程
            newcourse = Course.objects.create(course_name=course_name, max_select_num=max_select_num)
            # 在RC表中添加记录
            for resource_id in resource_ids:
                RC.objects.create(course_id=newcourse.id, resource_id=resource_id)
    except Exception:
        return JsonResponse({"code": "402", "msg": "数据库错误"})

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
    Course.objects.filter(id=this_id).delete()
    return JsonResponse({"code": "200", "msg": "ok"})
