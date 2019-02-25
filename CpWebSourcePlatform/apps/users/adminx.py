# _*_ coding: utf-8 _*_
# @Time     : 11:02
# @Author   : Amir
# @Site     : 
# @File     : adminx.py
# @Software : PyCharm


import xadmin
from xadmin import views
from .models import VerifyCode


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = "Amir博客后台"
    site_footer = "Amir聚合博客"
    menu_style = "accordion"


class VerifyCodeAdmin(object):
    list_diplay = '__all__'
    model_icon = 'fa fa-building-o'


xadmin.site.register(VerifyCode, VerifyCodeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)

xadmin.site.register(views.CommAdminView, GlobalSetting)
