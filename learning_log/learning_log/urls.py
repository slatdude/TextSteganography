"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
import django.contrib.auth.views
# import calculator.views
# import n_steg.views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'', include('learning_logs.urls', namespace='learning_logs')),
    # 学习笔记
    # url(r'^$', calculator.views.home, name='home'),
    # url(r'^compute/$', calculator.views.compute, name='compute'),  # 添加针对compute的路由
    # 计算器
    url(r'', include('n_steg.urls', namespace='n_steg')),
    # 文本隐写
]
