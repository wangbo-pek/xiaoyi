from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from BackEnd import models


# 确保响应中附带token
@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({"msg": "csrf token set"})


def get_article_list(request):
    print(request.body)
    print(request.GET)
    note_query_set = models.Note.objects.all()
    print(note_query_set)

    # 把数据转换为列表
    note_list = []
    for note_object in note_query_set:
        second_class_name = note_object.second_classification.name
        first_class_name = note_object.second_classification.first_classification.name
        tags_name = list(note_object.tags.values_list('name', flat=True))

        note_list.append({
            "title": note_object.title,
            "brief": note_object.brief,
            "content": note_object.content,
            "cover_item": "No more picture",
            "is_show": note_object.is_show,
            "created_time": note_object.created_time,
            "modified_time": note_object.modified_time,
            "tags": tags_name,
            "first_classification": first_class_name,
            "second_classification": second_class_name
        })

    return JsonResponse({
        "code": 0,
        "msg": "success",
        "data": note_list
    })
