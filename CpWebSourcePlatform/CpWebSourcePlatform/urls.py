"""CpWebSourcePlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin

from django.urls import path, include, re_path
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter

from CpWebSourcePlatform.settings import MEDIA_ROOT
from blog.views import BlogActicleBannerListViewSet, BlogActicleListViewSet, BlogCategoryListViewSet
from users.views import UserViewset, SmsCodeViewSet
from user_operation.views import UserFavViewSet, UserLeavingMessageViewSet, UserCommentViewSet

router = DefaultRouter()
router.register(r'users', UserViewset, base_name='user')
router.register(r'code', SmsCodeViewSet, base_name='code')
router.register(r'blogActicle', BlogActicleListViewSet, base_name='blogActicle')
router.register(r'blogActicleBanner', BlogActicleBannerListViewSet, base_name='blogActicleBanner')
router.register(r'blogCategory', BlogCategoryListViewSet, base_name='blogCategory')
router.register(r'userFavs', UserFavViewSet, base_name='userFavs')
router.register(r'userLeavingMessage', UserLeavingMessageViewSet, base_name='userLeavingMessage')
router.register(r'userComment', UserCommentViewSet, base_name='userComment')

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),

    # 文件
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),

    # drf文档，title自定义
    path('docs', include_docs_urls(title='Amir')),

    path('api-auth/', include('rest_framework.urls')),

    path('login/', obtain_jwt_token),

    path('', include(router.urls)),
]
