#-*- coding:utf-8 -*-

from django.views.decorators import csrf
from django.shortcuts import render

def login(request):
	context={}
	if request.POST:
		if request.POST.get("UserName",1) == "ymh" and request.POST.get("PassWord",2) == "ymh":
			context['user'] = request.POST.get("UserName",3)
			return render(request,"query.html",context)
		else:
			return render(request,"error_login.html")
	return render(request,"login.html")