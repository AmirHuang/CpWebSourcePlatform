# _*_ coding: utf-8 _*_
# @Time     : 11:03
# @Author   : Amir
# @Site     : 
# @File     : adminx.py
# @Software : PyCharm


import xadmin
from .models import UserFav, UserLeavingMessage, UserComment, AppProfile


class UserFavAdmin(object):
    list_display = ['user', 'acticle', "add_time"]
    model_icon = 'fa fa-cogs'


class UserLeavingMessageAdmin(object):
    list_display = ['user', "message", "add_time"]
    model_icon = "fa fa-comments-o"


class UserCommentAdmin(object):
    list_display = ["user", "acticle", "comment_content", "add_time"]
    model_icon = "fa fa-comments"


class AppProfileAdmin(object):
    list_display = ["file", "add_time"]
    model_icon = "fa fa-app"


xadmin.site.register(UserFav, UserFavAdmin)
xadmin.site.register(UserComment, UserCommentAdmin)
xadmin.site.register(UserLeavingMessage, UserLeavingMessageAdmin)
xadmin.site.register(AppProfile, AppProfileAdmin)
