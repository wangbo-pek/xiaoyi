from django.contrib import admin
from django.urls import path
import BackEnd.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # get请求，将csrf_token设置到浏览器的cookie中
    path('csrf/', BackEnd.views.get_csrf_token, name='get_csrf_token'),
    # 获取所有的笔记列表信息 NoteList
    path('getAllNoteList/', BackEnd.views.get_all_note_list, name='get_all_note_list'),
    # 根据noteListId，获取该文章所有的内容
    path('getNoteAllContent/', BackEnd.views.get_note_all_content, name='get_note'),
    # 获取所有的日记列表信息 DiaryList
    path('getAllDiaryList/', BackEnd.views.get_all_diary_list, name='get_all_diary_list'),
    # 根据diaryListId，获取该日记所有的内容
    path('getDiaryAllContent/', BackEnd.views.get_diary_all_content, name='get_diary_all_content'),
    # 获取博客网站的相关信息
    path('getBlogInfo/', BackEnd.views.get_blog_info, name='get_blog_info'),
    # 获取所有分类，并计算每个分类所对应的文章数量
    path('getAllCategoryCount/', BackEnd.views.get_all_category_count, name='get_all_category_count'),
    # 获取所有标签，并计算每个标签所对应的文章数量
    path('getAllTagCount/', BackEnd.views.get_all_tag_count, name='get_all_tag_count'),
]
