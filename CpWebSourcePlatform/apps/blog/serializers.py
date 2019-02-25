# _*_ coding: utf-8 _*_
# @Time     : 16:02
# @Author   : Amir
# @Site     : 
# @File     : serializers.py
# @Software : PyCharm

from rest_framework import serializers
from .models import BlogActicleBanner, BlogActicle, BlogCategory


class BlogActicleSerializers(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = BlogActicle
        fields = '__all__'


class BlogActiclePublicSerializers(serializers.ModelSerializer):
    class Meta:
        model = BlogActicle
        fields = ['acticle_name', 'acticle_sn', 'acticle_content']


class BlogActicleBannerSerializers(serializers.ModelSerializer):
    article = BlogActicleSerializers()

    class Meta:
        model = BlogActicleBanner
        fields = '__all__'


class BlogParentCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = '__all__'


class BlogCategorySerializers(serializers.ModelSerializer):
    sub_cat = BlogParentCategorySerializers(many=True)

    class Meta:
        model = BlogCategory
        fields = '__all__'
