from django.db.models import Sum, Count
from django.http import JsonResponse, HttpResponse
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
        note_list_query_set = models.NoteList.objects.all().order_by('-created_time')

        # 把数据转换为列表 (将QuerySet转换为List)
        note_list_data = []
        for note_list_object in note_list_query_set:
            tags_name = list(note_list_object.tags.values_list('name', flat=True))

            temp_created_time = note_list_object.created_time
            temp_modified_time = note_list_object.modified_time

            note_list_data.append({
                "noteListId": note_list_object.id,
                "title": note_list_object.title,
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
                "category": note_list_object.category.name,
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
        # 查询 NoteList 对象 (通过主键 ID 查找)
        note_list_obj = models.NoteList.objects.filter(id=note_list_id).first()
    except models.NoteList.DoesNotExist as e:
        return JsonResponse({
            "code": 1,
            "msg": f"note_list not found {e}"
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

    # 取出 note 实例
    note_obj = note_list_obj.note

    # 将返回的数据拼装为一个字典
    temp_created_time = note_list_obj.created_time
    temp_modified_time = note_list_obj.modified_time
    note_item = {
        "noteListId": note_list_obj.id,
        "title": note_list_obj.title,
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
        "category": note_list_obj.category.name,
        "markdownContent": note_obj.markdown_content,
        "imageUrls": note_obj.image_urls
    }

    return JsonResponse({
        "code": 0,
        "msg": "success",
        "data": note_item
    })


# 获取所有的日记列表信息 DiaryList
def get_all_diary_list(request):
    try:
        diary_list_query_set = models.DiaryList.objects.all().order_by('-created_time')

        # 把数据转换为列表 (将QuerySet转换为List)
        diary_list_data = []
        for diary_list_object in diary_list_query_set:
            temp_created_time = diary_list_object.created_time
            temp_modified_time = diary_list_object.modified_time

            diary_list_data.append({
                "diaryListId": diary_list_object.id,
                "title": diary_list_object.title,
                "brief": diary_list_object.brief,
                "coverImg": diary_list_object.cover_img,
                "isShow": diary_list_object.is_show,
                "createdTime": f"{temp_created_time.year}-{temp_created_time.month}-{temp_created_time.day}",
                "modifiedTime": f"{temp_modified_time.year}-{temp_modified_time.month}-{temp_modified_time.day}"
            })

        return JsonResponse({
            "code": 0,
            "msg": "success",
            "data": diary_list_data
        })
    except (ObjectDoesNotExist, DatabaseError) as e:
        return JsonResponse({
            "code": 1,
            "msg": f"failed{e}"
        })


# 根据diaryListId，获取该日记所有的内容
def get_diary_all_content(request):
    try:
        # 从请求中获取参数 diaryListId，并转换为 int 类型
        diary_list_id = int(request.GET.get('diaryListId'))
    except (TypeError, ValueError):
        return JsonResponse({
            "code": 1,
            "msg": "invalid diaryId"
        })

    try:
        # 查询 DiaryList 对象 (通过主键 ID 查找)
        diary_list_obj = models.DiaryList.objects.filter(id=diary_list_id).first()
    except models.DiaryList.DoesNotExist as e:
        return JsonResponse({
            "code": 1,
            "msg": f"diary_list not found {e}"
        })
    except (DatabaseError, FieldError) as e:
        return JsonResponse({
            "code": 1,
            "msg": f"failed{e}"
        })

    if not hasattr(diary_list_obj, 'diary'):
        return JsonResponse({
            "code": 1,
            "msg": "diary not found"
        })

    # 取出 diary 实例
    diary_obj = diary_list_obj.diary

    # 将返回的数据拼装为一个字典
    temp_created_time = diary_list_obj.created_time
    temp_modified_time = diary_list_obj.modified_time
    diary_item = {
        "diaryListId": diary_list_obj.id,
        "title": diary_list_obj.title,
        "brief": diary_list_obj.brief,
        "coverImg": diary_list_obj.cover_img,
        "isShow": diary_list_obj.is_show,
        "createdTime": f"{temp_created_time.year}-{temp_created_time.month}-{temp_created_time.day}",
        "modifiedTime": f"{temp_modified_time.year}-{temp_modified_time.month}-{temp_modified_time.day}",
        "markdownContent": diary_obj.markdown_content,
        "imageUrls": diary_obj.image_urls
    }

    return JsonResponse({
        "code": 0,
        "msg": "success",
        "data": diary_item
    })


# 获取博客网站的相关信息
def get_blog_info(request):
    try:
        blog_info_obj = models.BlogInfo.objects.all().first()
        blog_info_obj.blog_viewed_count += 1
        blog_info_data = {
            "blogName": blog_info_obj.blog_name,
            "blogArticlesCount": models.NoteList.objects.count(),
            "blogWordsCount": blog_info_obj.blog_words_count,
            "blogViewedCount": blog_info_obj.blog_viewed_count,
            "blogDurationRunning": blog_info_obj.blog_duration_running,
        }
        blog_info_obj.save(update_fields=['blog_viewed_count'])

        return JsonResponse({
            "code": 0,
            "msg": "success",
            "data": blog_info_data
        })
    except (ObjectDoesNotExist, DatabaseError) as e:
        return JsonResponse({
            "code": 1,
            "msg": f"failed{e}"
        })


# 获取所有文章分类，并计算每个分类所对应的文章数量
def get_all_category_count(request):
    categories = models.Category.objects.annotate(note_count=Count('notelist__note')).values('name', 'note_count')

    category_count = []
    for category in categories:
        category_count.append({
            "category": category['name'],
            "note_count": category['note_count']
        })

    return JsonResponse({
        "code": 0,
        "msg": "success",
        "data": category_count
    })


# 获取所有文章标签，并计算每个标签所对应的文章数量
def get_all_tag_count(request):
    tags = models.Tag.objects.annotate(note_count=Count('notelist__note')).values('name', 'note_count')

    tag_count = []
    for tag in tags:
        tag_count.append({
            "tag": tag['name'],
            "tag_count": tag['note_count']
        })

    return JsonResponse({
        "code": 0,
        "msg": "success",
        "data": tag_count
    })
