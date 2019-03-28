import re

from rest_framework import serializers
from Restapp1.models import Actor

# class ActorSerializers(serializers.ModelSerializer):
#     """演员序列化器"""
#
#     class Meta:
#         model = Actor
#         fields = '__all__'
def v_Age(value):
    reg = r'^[123]\d{1}$'
    v = str(value)
    if not re.match(reg,v):
        raise serializers.ValidationError("age 字段值必须在10-40之间")



class ActorSerializers(serializers.Serializer):
    GENDER_ID=(
        ('0','男'),('1','女')
    )
    """
    演员表的序列化器
    
    """                 #read_only表明该字段仅用于序列化输出

    aid = serializers.IntegerField(label='编号',read_only=True)
    aname = serializers.CharField(label='姓名',max_length=30)
    #required 反序列化时必须输入  默认True
    age = serializers.IntegerField(label='年龄',required=False,validators=[v_Age])
    agender = serializers.ChoiceField(choices=GENDER_ID,label='性别',required=False)
    birth_date = serializers.DateField(label='出生年月',required=False)
    photo = serializers.ImageField(label='头像',required=False)
    def create(self, validated_data):
        return Actor.objects.create(**validated_data)


class MovieSerializer(serializers.Serializer):
    mid = serializers.IntegerField(label='影片编号',read_only=True)
    mname = serializers.CharField(label='影片名称',max_length=30)
    m_pub_date = serializers.DateField(label='上映日期',required=False)
    mread = serializers.IntegerField(label='阅读量')
    mcomment = serializers.CharField(label='评论',max_length=300,required=False,allow_null=True)
    mimage = serializers.ImageField(label='图片',required=False)
    actors = serializers.PrimaryKeyRelatedField(label='演员',read_only=True)
    # actors = serializers.PrimaryKeyRelatedField(label='演员',queryset=Actor.objects.all())
    # actors = ActorSerializers()
    actors =serializers.StringRelatedField(label='演员')