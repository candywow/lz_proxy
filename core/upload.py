#!/usr/bin/python2.7  
# -*- coding: utf-8 -*- 

import os
import re
import start_lizheng_proxy
# data to transfer
dirfile="/home/ubuntu/file_sync/lizheng_file"
#原始数据/"
dirfile=unicode(dirfile , "utf8")

class Updatedata(object):

	def __init__(self,dirfile):

		self.dir = dirfile
		self.k=[]
		
	def get_filelist(self,dir):
		self.filelist=os.listdir(self.dir)
		for self.file in self.filelist:
			self.p=re.compile('\d+')
			if not self.p.search(self.file):
				self.k.append(self.file)
		for x in self.k:
			self.filelist.remove(x)
		return self.filelist

	def print_filelist1(self,filelist):
		f=open(self.dir+"/"+"filelist.txt",'w')
		f.write(str(len(self.filelist)))
		f.close

class Process(object):

	def __init__(self,file,dirfile):
		self.file=file
		self.dir=dirfile
		self.p = None

	def get_date(self,file):
		self.p=re.compile(r'\d+')
		self.date=self.p.findall(self.file)
		self.date_new='%s-%s-%s:%s-%s-%s'%(self.date[0],self.date[1],self.date[2],self.date[3],self.date[4],self.date[5])

		return self.date_new

	def get_text(self,dir,file):
		self.f=open(self.dir+"/"+self.file,"r")
		self.rawdata=self.f.read()
		self.f.close

		return self.rawdata

	def get_transmitter(self,rawdata):
		self.p=re.compile(r'FYLZ\d+')
		self.transmitter=self.p.findall(self.rawdata)

		return self.transmitter

	def get_line(self,rawdata):
		try:
			self.d=re.compile(r'SM\r\s.*\r\s.*\r')
			self.line=self.d.findall(self.rawdata)
		except:print "re error"

		return self.line

upload = Updatedata(dirfile)

if os.path.exists('filelist.txt'):
	f=open('filelist.txt','r')
	filelist=f.readline()
	f.close
	filelist1_lenth=int(filelist)
	#print filelist1_lenth
else:
	# os.mknod('D:\project\利正卫星数据\测试数据/text.txt')
	f = open('filelist.txt','w')
	f.write(str(0))
	f.close
	filelist1_lenth=int(0)
	#print filelist1_lenth

filelist2=upload.get_filelist(dirfile)
filelist2_lenth =len(filelist2)
#print filelist2_lenth

if len(filelist2)!=filelist1_lenth:

	filelist2.sort(key=lambda x:os.path.getmtime(dirfile+"/"+x))#sort the file by time
	count=len(filelist2)-filelist1_lenth
	#get the new message that didnt write before

	n=count
	print n
	while n>=1:
		
		filelist1_lenth += 1
		new_file=filelist2[-n]
		process=Process(new_file,dirfile)
		date=process.get_date(new_file)#get the date of receive message
		#print date
		transmitter_list=process.get_transmitter(process.get_text(dirfile,new_file))#get the transmitter names
		#print transmitter_list
		line = process.get_line(process.get_text(dirfile,new_file))#get the content of one message
		#print line
		lenth=len(transmitter_list)#get the transmitter number
		print lenth
		#process when data is null
		url = '202.120.58.126'
		username = 'admin'
		password = 'omnilab'
		proxy = start_lizheng_proxy.ProxyStart(url, username, password)
		proxy.proxy_start()
		#try:
		k = 0
		while k<lenth:
			#print ' '
			#print line[k]
			#print ' '
			content = line[k]
			content_list = content.split('\n')
			if len(content_list) < 3:
				content_list.append("None")
	#		print content_list
			data_temp=[]
			data_temp.append(content_list[1])
			data=[{
				"date":date,
				"transmitter":transmitter_list[k],
				"head":str(data_temp),
				"data":content_list[2],
				}]
			#datastore_upsert(resource_id, data, api_key)
			#lizheng_proxy.main(data)
			print data
			proxy.proxy_publish(data)
			#print data
			k+=1 
		#except:print "updata to ckan error"
		
		f=open('filelist.txt','w')
		f.write(str(filelist1_lenth))
		f.close
		n-=1