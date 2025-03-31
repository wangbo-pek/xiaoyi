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
def get_all_note_list(request):
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


# 根据noteListId，获取该文章所有的内容
def get_note_all_content(request):
    try:
        # 从请求中获取参数 noteListId，并转换为 int 类型
        note_list_id = int(request.GET.get('noteListId'))
    except (TypeError, ValueError):
        return JsonResponse({
            "code": 1,
            "msg": "invalid noteId"
        })

    try:
        # 查询 NoteList 对象（通过主键 ID 查找）
        note_list_obj = models.NoteList.objects.filter(id=note_list_id).first()
    except models.NoteList.DoesNotExist as e:
        return JsonResponse({
            "code": 1,
            "msg": 'notelist not found'
        })
    except (DatabaseError, FieldError) as e:
        return JsonResponse({
            "code": 1,
            "msg": f"failed({e})"
        })

    if not hasattr(note_list_obj, 'note'):
        return JsonResponse({
            "code": 1,
            "msg": "note not found"
        })

    # 取出note实例
    note_obj = note_list_obj.note

    # 将返回的数据拼装为一个字典
    temp_created_time = note_list_obj.created_time
    temp_modified_time = note_list_obj.modified_time
    note_item = {
        "noteListId": note_list_obj.id,
        "title": note_list_obj.title,
        "subtitle": note_list_obj.subtitle,
        "brief": note_list_obj.brief,
        "coverImg": note_list_obj.cover_img,
        "isShow": note_list_obj.is_show,
        "isPinned": note_list_obj.is_pinned,
        "isRecommended": note_list_obj.is_recommended,
        "viewedCount": note_list_obj.viewed_count,
        "likedCount": note_list_obj.liked_count,
        "disgustedCount": note_list_obj.disgusted_count,
        "createdTime": f"{temp_created_time.year}-{temp_created_time.month}-{temp_created_time.day}",
        "modifiedTime": f"{temp_created_time.year}-{temp_modified_time.month}-{temp_modified_time.day}",
        "tagsName": list(note_list_obj.tags.values_list('name', flat=True)),
        "firstClassification": note_list_obj.second_classification.first_classification.name,
        "secondClassification": note_list_obj.second_classification.name,
        "markdownContent": note_obj.markdown_content,
        "tableOfContent": note_obj.table_of_content,
        "imageUrls": note_obj.image_urls
    }

    return JsonResponse({
        "code": 0,
        "msg": "success",
        "data": note_item
    })
