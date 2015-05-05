#! /usr/bin/env python
# -*- coding=UTF-8 -*-

'''
    configuration of LiZhengProxy
    @author: Jieyi Wang
    @email: jiezhen@sjtu.edu.cn
'''
import lib.sensor as sensor
import lib.proxy as proxy
import json  

class ProxyConfig:
	def __init__(self, config_path, proxy):
		self._config_dict = None
		self._config_path = config_path
		self._proxy = proxy

	def load(self):
		with open(self._config_path) as f:
			self._config_dict = json.loads(f.read())

	def get_sensor_list(self):
		sensors = self._config_dict['sensors']
		for s in sensors:
			sensor_tmp = sensor.sensor(s['sensor_uuid'],s['sensor_name'],s['sensor_type'],s['sensor_unit'])
			proxy.add_sensor
#config_path = 'lizheng_proxy.json'
#c = ProxyConfig(config_path)
#c.load()
#print c.get('api_key')
