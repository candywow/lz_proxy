#! /usr/bin/env python
# -*- coding=UTF-8 -*-

'''
    configuration of Proxy
    @author: Jieyi Wang
    @email: jiezhen@sjtu.edu.cn
'''
import lib.sensor as sensor
import lizheng_proxy
import json  

class ProxyConfig:
	def __init__(self, config_path):
		self._config_dict = None
		self._config_path = config_path
		self._proxy = None

	def load(self):
		with open(self._config_path) as f:
			self._config_dict = json.loads(f.read())

	def get_proxy(self):
		if self._proxy != None:
			return self._proxy
		self._process()
		return self._proxy

	def _process(self):
		if self._config_dict['hub_type'] == 'lizheng':
			self._proxy = lizheng_proxy.LiZhengProxy()
			self._proxy.set_api_key(self._config_dict['api_key'])
			self._proxy.set_hub_uuid(self._config_dict['hub_uuid'])
			self._proxy.set_hub_name(self._config_dict['hub_name'])
			sensors = self._config_dict['sensors']
			for s in sensors:
				#print s
				sensor_tmp = sensor.sensor(s['sensor_uuid'], s['sensor_name'], 
					s['sensor_type'], s['sensor_unit'])
				#print sensor_tmp.get_sensor_name()
				self._proxy.add_sensor(sensor_tmp)

			#print self._proxy.get_api_key()
			#print self._proxy.get_hub_uuid()
			#print self._proxy.get_hub_name()
			#sensors = self._proxy.get_sensor_list()
			#for s in sensors:
			#	print s.get_sensor_name

#config_path = 'lizheng_proxy.json'
#c = ProxyConfig(config_path)
#c.load()
#p = c.get_proxy()
#print p.get_api_key()
#print p.get_hub_uuid()
#print p.get_hub_name()
#sensors = p.get_sensor_list()
#for s in sensors:
#	print s.get_sensor_name()


