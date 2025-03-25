from django.contrib import admin
from django.urls import path
import BackEnd.views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # get请求，将csrf_token设置到浏览器的cookie中
    path('csrf/', BackEnd.views.get_csrf_token, name='get_csrf_token'),
    # 获取所有的笔记列表信息 NoteList
    path('getNoteList/', BackEnd.views.get_note_list, name='get_note_list'),
    # 根据note list id，获取相关联的note content
    path('getNote/', BackEnd.views.get_note, name='get_note')
]
