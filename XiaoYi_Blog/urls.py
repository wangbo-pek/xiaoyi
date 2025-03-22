from django.contrib import admin
from django.urls import path
import BackEnd.views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('test/', BackEnd.views.test, name='test'),

    #
    path('csrf/', BackEnd.views.get_csrf_token, name='get_csrf_token')
]
