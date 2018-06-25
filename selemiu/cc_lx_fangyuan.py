#coding:utf-8

import time,os,sys,chardet
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import json
import pymysql
import smtplib
import email.mime.text
import traceback
from email.utils import parseaddr, formataddr
from email import encoders
from email.header import Header
import urllib3

HOST = 'smtp.gmail.com'
PORT = 587
mail_username='yanxingyang@gmail.com'  
mail_password='linshimima' 

to_addrs=['yanxingyang@gmail.com'] 

urls = [r"http://www.bjjs.gov.cn/bjjs/fwgl/zzxspzf/tzgg/index.shtml"]

def sendmail(contents,title):
	try:
		smtp = smtplib.SMTP() 
		smtp.set_debuglevel(1)
		smtp.connect(HOST,PORT)
		smtp.starttls()
		smtp.login(mail_username,mail_password)
		msg = email.mime.text.MIMEText(contents,'html')
		msg['From'] = 'yanxingyang@gmail.com'
		msg['To'] = ';'.join(to_addrs)  
		msg['Subject']=  '有新的房产信息,请注意查看《%s》'% title   
		smtp.sendmail('yanxingyang@gmail.com',to_addrs,msg.as_string())  
	except:
		print (traceback.format_exc())
	finally:
		smtp.quit()

def executesql(sql):
	dbo  = pymysql.connect("localhost","root","password","houseinfo")
	cursor = dbo.cursor()
	data = ''
	try:
		cursor.execute(sql)
		if sql.startswith('select'):
			data = cursor.fetchall()
		elif sql.startswith('insert'):
			data = dbo.commit()
	except:
		print ("Error: unable to fecth data")
		print (traceback.format_exc())
		dbo.rollback()
	finally:
		dbo.close()		
		return data

def main():
	for url in urls:
		# r = requests.get(url)
		s = urllib3.request.urlopen(url)
		if s.code == 200:
			soup = BeautifulSoup(s.read(),"lxml")
			ulcontent = soup.find('ul',opentype="page")	
			for i in ulcontent.children:
				acontent = i.find('a')
				if type(acontent)!=int:
					title = acontent.get('title').encode('utf-8')
					if acontent.get('href').startswith(r'/'):
						url = "%s%s"%(r'http://www.bjjs.gov.cn',acontent.get('href'))						
					else:
						url = acontent.get('href')

					sql = 'select * from house where url = "%s"'% url
					rst = executesql(sql)
					if not rst:
						insertsql = 'insert into house (url,title) values("%s","%s")'%(url,title)
						executesql(insertsql)
						contents = '<h1>%s</h1></br><p>%s</p>'%(title,url)
						sendmail(contents,title)

if __name__ == '__main__':
	main()