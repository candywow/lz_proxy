#! /usr/bin/env python
# -*- coding=UTF-8 -*-

'''
    class of LiZhengProxy
    @author: Jieyi Wang
    @email: jiezhen@sjtu.edu.cn
'''

#import json
import lib.module_ckan as module_ckan
#import lib.mqpp_api as mqpp_api
import lib.proxy as proxy
import module_data_parse

class LiZhengProxy(proxy.proxy):

	def __init__(self):
		proxy.proxy.__init__(self)

	def get_data(self):
		api_key = 'dbf651ea-71cf-4c78-844a-8f7bf3db81e2'
		resource_id = '60000630-f011-4040-bbae-29f7e63e5a5c'

		ckan_lizheng = module_ckan.ckan(server_address, api_key, resource_id)
		self._meta_data = ckan_lizheng.get_data(1, 3)
		#print self.meta_data
		#print self.meta_data['data']
		return True

	def parse_data(self):
		#self.LiZhengProxy_name = self.meta_data[0]['transmitter']
		data = module_data_parse.data_parse(self._meta_data[0]['data'])
		date = module_data_parse.time_parse(self._meta_data[0]['date'])
		location = module_data_parse.location_parse(self._meta_data[0]['head'])

		for s in self._sensor_list:
			s.set_sensor_value(data[s.get_sensor_name()])
			s.set_datetime(date)
			s.set_longitude(location['x'])
			s.set_latitude(location['y'])
			#print s.get_sensor_name()
			#print s.get_sensor_value()
			#print s.get_datetime()
			#print s.get_longitude()
			#print s.get_latitude()
		return True

	#def run_proxy(self, url, username, password):
	#	self.get_data()
	#	self.parse_data()
	#	self.pack_sensor_data()
	#	self.connect(url, username, password)
	#	self.push_data()



		
