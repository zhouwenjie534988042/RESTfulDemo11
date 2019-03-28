import json
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework import mixins

from Restapp1.models import *





from Restapp1.models import Actor
from rest_framework.viewsets import ModelViewSet

from Restapp1.serializers import ActorSerializers

from rest_framework.utils.serializer_helpers import
from  rest_framework.generics import GenericAPIView
class ActorListView(mixins.CreateModelMixin,GenericAPIView):
    """
    查询所有演员信息、增加演员信息、修改、删除操作
    """
    # actors = Actor.objects.all()
    #
    # actorsObj = ActorSerializers(actors,many=True)
    # actorsObj.data

    queryset = Actor.objects.all()
    serializer_class = ActorSerializers
    def post(self,request):
        return self.create(request)
# class ActorListView(View):
#     def get(self,request):
#         #查数据  路由： GET /actors/
#         queryset = Actor.objects.all()
#
#         #遍历取出数据
#         actor_list =  []
#
#         for actor in queryset:
#             actor_list.append({
#                 'aid': actor.aid,
#                 'aname': actor.aname,
#                 'age': actor.age,
#                 'agender': actor.agender,
#                 'birth_date': actor.birth_date,
#                 'photo': actor.photo.url if actor.photo else ''
#
#             })
#         return JsonResponse(actor_list, safe=False)
#
#     def post(self, request):
#         """
#         新增演员信息
#
#         路由： POST /actors/
#         """
#         #获取用户要增加的请求数据 ---获取到是byte数据---》str--->dict
#         json_bytes = request.body
#         #解码后为 str类型
#         json_str = json_bytes.decode()
#         #编码为json格式的字典
#         actor_dict = json.loads(json_str)
#
#         #吧获取到的数据写入数据库
#         actor = Actor.objects.create(
#             aname = actor_dict.get('aname'),
#             age = actor_dict.get('age'),
#             agender = actor_dict.get('agender'),
#             birth_date = actor_dict.get('birth_date')
#         )
#         #返回给响应页面
#         return JsonResponse({
#                 'aid':actor.aid,
#                 'aname':actor.aname,
#                 'age':actor.age,
#                 'agender':actor.agender,
#                 'birth_date':actor.birth_date,
#                 'photo':actor.photo.url if actor.photo else ''
#
#             },status=201)
