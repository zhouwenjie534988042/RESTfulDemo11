from django.conf.urls import url, include
from django.contrib import admin

from Restapp1 import views
from rest_framework.routers import DefaultRouter
urlpatterns = [
    # url(r'^actors/$', views.ActorListView.as_view({'post':'create'})),
    # url(r'^actors/(?P<pk>\d+)$', views.ActorListView.as_view()),
]

# router  = DefaultRouter() # 可以处理视图的路由器
#                 #地址        视图类
# router.register('actors',views.ActorListView,basename='actors')  # 向路由器中注册视图集
# print(router.urls)
# urlpatterns += roter.urls  # 将路由器中的所以路由信息追到到django的路由列表中
