from django.contrib import admin
from django.urls import path
import BackEnd.views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # get请求，将csrf_token设置到浏览器的cookie中
    path('csrf/', BackEnd.views.get_csrf_token, name='get_csrf_token'),
    path('getArticleList/', BackEnd.views.get_article_list, name='get_article_list')
]
