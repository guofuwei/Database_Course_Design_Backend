from django.http import JsonResponse
import platform


def reset(request):
    if request.method != "POST":
        return JsonResponse({"code": "400", "msg": "请求方法错误"})
    if platform.system() == "Linux":
        import os
        res = os.system("/home/hanshan/restore.sh")
        if res == 0:
            return JsonResponse({"code": "200", "msg": "ok"})
        else:
            return JsonResponse({"code": "401", "msg": "重置数据库失败"})
    else:
        return JsonResponse({"code": "201", "msg": "非生产环境，无法重置数据库"})
