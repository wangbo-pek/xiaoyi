from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.exceptions import ObjectDoesNotExist, FieldError
from django.db import DatabaseError
from BackEnd import models


# 确保响应中附带token
@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({"msg": "csrf token set"})


# 获取所有的笔记列表信息 NoteList
def get_note_list(request):
    try:
        note_list_query_set = models.NoteList.objects.all()

        # 把数据转换为列表 (将QuerySet转换为List)
        note_list_data = []
        for note_list_object in note_list_query_set:
            second_classification = note_list_object.second_classification.name
            first_classification = note_list_object.second_classification.first_classification.name
            tags_name = list(note_list_object.tags.values_list('name', flat=True))

            temp_created_time = note_list_object.created_time
            temp_modified_time = note_list_object.modified_time

            note_list_data.append({
                "noteListId": note_list_object.id,
                "title": note_list_object.title,
                "subtitle": note_list_object.subtitle,
                "brief": note_list_object.brief,
                "coverImg": note_list_object.cover_img,
                "isShow": note_list_object.is_show,
                "isPinned": note_list_object.is_pinned,
                "isRecommended": note_list_object.is_recommended,
                "viewedCount": note_list_object.viewed_count,
                "likedCount": note_list_object.liked_count,
                "disgustedCount": note_list_object.disgusted_count,
                "createdTime": f"{temp_created_time.year}-{temp_created_time.month}-{temp_created_time.day}",
                "modifiedTime": f"{temp_modified_time.year}-{temp_modified_time.month}-{temp_modified_time.day}",
                "tagsName": tags_name,
                "firstClassification": first_classification,
                "secondClassification": second_classification
            })

        return JsonResponse({
            "code": 0,
            "msg": "success",
            "data": note_list_data
        })
    except (ObjectDoesNotExist, DatabaseError) as e:
        return JsonResponse({
            "code": 1,
            "msg": f"failed({e})"
        })


# 根据note list id，获取相关联的note content
def get_note(request):
    try:
        note_list_id = int(request.GET.get('noteListId'))
    except (TypeError, ValueError):
        return JsonResponse({
            "code": 1,
            "msg": "invalid noteId"
        })

    try:
        note_list_obj = models.NoteList.objects.filter(id=note_list_id).first()
    except (DatabaseError, FieldError) as e:
        return JsonResponse({
            "code": 1,
            "msg": f"failed({e})"
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
            "content": note_obj.markdown_content,
            "title": note_obj.title
        }
    })
