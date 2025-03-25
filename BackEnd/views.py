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
            "id": note_list_object.id,
            "title": note_list_object.title,
            "brief": note_list_object.brief,
            "coverImg": note_list_object.cover_img,
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


def get_article(request):
    try:
        note_list_id = int(request.GET.get('noteId'))
    except (TypeError, ValueError):
        return JsonResponse({
            "code": 1,
            "msg": "invalid noteId"
        })

    try:
        note_list_obj = models.NoteList.objects.filter(id=note_list_id).first()
    except Exception:
        return JsonResponse({
            "code": 1,
            "msg": "failed"
        })

    if not note_list_obj or not hasattr(note_list_obj, 'note'):
        return JsonResponse({
            "code": 1,
            "msg": "note not found"
        })
    note_obj = note_list_obj.note
    return JsonResponse({
        "code": 0,
        "msg": "success",
        "data": {
            "content":note_obj.content,
            "title":note_obj.title
        }
    })
