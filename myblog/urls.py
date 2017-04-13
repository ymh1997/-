#-*- coding:utf-8 -*-

from django.conf.urls import url
from django.contrib import admin
from . import view,testdb,search,search2,login,query   #从当前的路径中import 这些模块

urlpatterns = [
     url(r'^hello$',view.hello),
     url(r'^testdb$',testdb.testdb),
     url(r'^admin/',admin.site.urls),
     url(r'^search-form$',search.search_form),
     url(r'^search$',search.search),        #注意每一行的后面不要少了','
     url(r'^search-post$',search2.search_post),
     url(r'^login$',login.login),
     url(r'^query$',query.query),
     #url(r'^error_login$'),
]

#这个url脚本是用于处理url的，所有可用的url以list的形式储存在urlpatterns中，url函数的第一个参数为用于匹配的正则表达式，后面的参数的意思是执行与正则表达所匹配的URL请求

