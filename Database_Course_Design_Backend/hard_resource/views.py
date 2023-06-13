from django.http import JsonResponse
from .models import HardResource
import json
from utils.utils import make_res


# Create your views here.
def test(request):
    return JsonResponse({"message": "Hello, world!"})


def get_all(request):
    if request.method != "GET":
        return JsonResponse({"code": "400", "msg": "请求方法错误"})
    hard_resource = HardResource.objects.all()
    res = make_res(hard_resource, "hard_resource")
    return JsonResponse({"code": "200", "data": res})


def get_by_filter(request):
    if request.method != "GET":
        return JsonResponse({"code": "400", "msg": "请求方法错误"})
    # 获取get params
    this_id = request.GET.get("id")
    resource_name = request.GET.get("resourceName")
    # 用上述不为空的值构建filter字典
    filter_dict = {}
    if this_id is not None:
        filter_dict["id"] = this_id
    if resource_name is not None:
        filter_dict["resource_name"] = resource_name
    # 用filter字典查询
    hard_resource = HardResource.objects.filter(**filter_dict)
    res = make_res(hard_resource, "hard_resource")
    return JsonResponse({"code": "200", "data": res})


def add(request):
    if request.method != "POST":
        return JsonResponse({"code": "400", "msg": "请求方法错误"})
    # 获取post body
    body = request.body
    # 解析json格式的body
    body = json.loads(body)
    # 获取body中的参数
    resource_name = body.get("resourceName")
    resource_num = body.get("resourceNum")
    # 当有参数为空，返回错误
    if body is None or resource_name is None or resource_num is None:
        return JsonResponse({"code": "401", "msg": "参数错误"})
    # 新建学生
    HardResource.objects.create(resource_name=resource_name, resource_num=resource_num)
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
    HardResource.objects.filter(id=this_id).delete()
    return JsonResponse({"code": "200", "msg": "ok"})
