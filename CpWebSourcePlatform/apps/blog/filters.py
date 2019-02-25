# _*_ coding: utf-8 _*_
# @Time     : 16:09
# @Author   : Amir
# @Site     : 
# @File     : filters.py
# @Software : PyCharm

import django_filters
from django_filters import rest_framework as filters
from .models import BlogActicle


class BlogActicleFilter(filters.FilterSet):
    acticle_name = django_filters.CharFilter(name='acticle_name', lookup_expr='icontains', help_text="文章名")
    acticle_content = django_filters.CharFilter(name='acticle_content', lookup_expr='icontains', help_text="文章内容")

    class Meta:
        model = BlogActicle
        fields = ('acticle_name', 'acticle_content')
