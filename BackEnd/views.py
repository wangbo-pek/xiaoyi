from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie


def test(request):
    if request.method == 'GET':
        print(request.GET)
        print(request.body)
        return JsonResponse({"msg":"get_test"})
    elif request.method == 'POST':
        print(request.POST)
        print(request.body)
        return JsonResponse({"msg":"post_test"})


# 确保响应中附带token
@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({"msg":"csrf token set"})