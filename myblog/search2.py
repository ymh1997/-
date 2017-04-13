#-*- coding:utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf

#接受POST请求数据
def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST.get('q',403)   #ctx(context)字典的key即是html文件中预留的变量的名字 
    return render(request,"post.html",ctx)
