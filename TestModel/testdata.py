#-*- coding:utf-8 -*-
#!/usr/bin/env python3

import pymysql
import numpy as np
from datetime import datetime
import e_mail
import time

db = pymysql.connect("localhost","root","ymh5852201+","WEB1")
cursor = db.cursor()

while(1):
	data = float(np.random.randint(0,100)*0.1+20)
	now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	#if data > 25.0:
	#	e_mail.send(str(data))

	sql = """INSERT INTO TestModel_temperature
	(value_of_temperature,date_time)
	VALUES('%f','%s')
	"""%(data,now)

	try:	
		cursor.execute(sql)
		db.commit()
	except :
		db.rollback()
	time.sleep(60)	#Every 60s insert a value into database
db.close()

