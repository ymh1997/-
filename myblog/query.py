#-- coding:utf-8 --

import pymysql
from django.views.decorators import csrf
from django.shortcuts import render
from datetime import datetime
import matplotlib.pyplot as plt

def plots(dates,values):
	fig = plt.figure()
	plt.xlabel("DateTime")
	plt.ylabel("Temperature")
	plt.title("figure")
	plt.plot(dates,values)
	plt.savefig('/home/ymh/myblog/TestModel/static/simple1_plot.png')		


def query(request):
	context = {}
	if request.POST:
		StartYear = int(request.POST.get("start_year"))
		StartMonth = int(request.POST.get("start_month"))
		StartDay = int(request.POST.get("start_day"))
		StartHour = int(request.POST.get("start_hour"))
		StartMinute = int(request.POST.get("start_minute"))
		StartSecond = int(request.POST.get("start_second"))

		EndYear = int(request.POST.get("end_year"))
		EndMonth = int(request.POST.get("end_month"))
		EndDay = int(request.POST.get("end_day"))
		EndHour = int(request.POST.get("end_hour"))
		EndMinute = int(request.POST.get("end_minute"))
		EndSecond = int(request.POST.get("end_second"))
		try:
			StartTime = datetime(StartYear,StartMonth,StartDay,StartHour,StartMinute,StartSecond).strftime('%Y-%m-%d %H:%M:%S')
			EndTime = datetime(EndYear,EndMonth,EndDay,EndHour,EndMinute,EndSecond).strftime('%Y-%m-%d %H:%M:%S')
		except:
			context['result_of_query'] = "请检查您所输入的时间，您可能输入了错误的时间，例如2017-2-31 22：23：24!"
			context['flag'] = False
			return render(request,"query.html",context)
		# Handle in database
		db = pymysql.connect("localhost","root","ymh5852201+","WEB1")	#connect to mysql database
		cursor = db.cursor()							#create a cursor

		sql = """SELECT * FROM TestModel_temperature \
			WHERE  unix_timestamp(date_time) >= unix_timestamp('%s') and \
			unix_timestamp(date_time) <= unix_timestamp('%s') \
			ORDER BY date_time DESC"""%(StartTime,EndTime)

		try:
			cursor.execute(sql)
			results = cursor.fetchall()
			if results == ():
				context['result_of_query'] = "您查询的时间段内无记录!" 
				#context['flag'] = StartTime + '\n' +EndTime
				context['flag'] = False
				return render(request,"query.html",context)
			else:
				context['result_of_query'] = "以下是您查询的数据: "
				context['flag'] = True
				context['StartTime'] = StartTime
				context['EndTime'] = EndTime
				data = []
				#value = []
				#date = []

				for row in results:
					data.append({row[2].strftime('%Y-%m-%d %H:%M:%S'):row[1]})
					#dates.append(row[2])
					#values.append(row[1])

				#plots(dates,values)
				context['data'] = data

				return render(request,"query.html",context)

		except :
			context['result_of_query'] = "未知的错误发生了，请联系管理员!" 
			context['flag'] = False
			return render(request,"query.html",context)
		

	else:	
		context['user'] = "Sorry! You are NOT logged in!"
		return render(request,"login.html",context,{'date':date})

