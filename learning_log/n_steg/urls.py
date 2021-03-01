"""定义n_steg的URL模式"""

from django.conf.urls import url
from . import views

urlpatterns = [
    # 主页(信息介绍页）
    url(r'^$', views.info, name='info'),
    # 加密
    url(r'^encrypt/$', views.encrypt, name='encrypt'),
    # 解密
    url(r'^decrypt/$', views.decrypt, name='decrypt'),
]