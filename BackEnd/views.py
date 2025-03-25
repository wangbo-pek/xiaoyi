from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from BackEnd import models


# 确保响应中附带token
@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({"msg": "csrf token set"})


def get_article_list(request):
    note_list_query_set = models.NoteList.objects.all()
    print(note_list_query_set)

    # 把数据转换为列表
    note_list_data = []
    for note_list_object in note_list_query_set:
        second_classification = note_list_object.second_classification.name
        first_classification = note_list_object.second_classification.first_classification.name
        tags_name = list(note_list_object.tags.values_list('name', flat=True))

        note_list_data.append({
            "title": note_list_object.title,
            "brief": note_list_object.brief,
            # ImageFieldFile类型不能序列化
            "coverImg": note_list_object.cover_img.url if note_list_object.cover_img else "",
            "isShow": note_list_object.is_show,
            "createdTime": note_list_object.created_time,
            "modifiedTime": note_list_object.modified_time,
            "tagsName": tags_name,
            "firstClassification": first_classification,
            "secondClassification": second_classification
        })

    return JsonResponse({
        "code": 0,
        "msg": "success",
        "data": note_list_data
    })
