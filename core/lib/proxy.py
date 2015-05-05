#! /usr/bin/env python
# -*- coding=UTF-8 -*-

'''
    base class of proxy
    @author: Jieyi Wang
    @email: jiezhen@sjtu.edu.cn
'''

import json
import mqpp_api

class proxy(object):

	def __init__(self, api_key="None", hub_uuid="None", 
				hub_name="None", meta_data="None", sensor_list=[]):
		self._api_key = api_key
		self._hub_uuid = hub_uuid
		self._hub_name = hub_name
		self._sensor_list = sensor_list
		self._meta_data = meta_data
		self._sensor_data_list = []
		self._channel = None

	def set_api_key(self, api_key):
		self._api_key = api_key

	def get_api_key(self):
		return self._api_key

	def set_hub_uuid(self, hub_uuid):
		self._hub_uuid = hub_uuid	

	def get_hub_uuid(self):
		return self._hub_uuid

	def set_hub_name(self, hub_name):
		self._hub_name = hub_name

	def get_hub_name(self):
		return self._hub_name

	def set_sensor_list(self, sensor_list):
		self._sensor_list = sensor_list

	def get_sensor_list(self):
		return self._sensor_list

	def set_meta_data(self, meta_data):
		self._meta_data = meta_data

	def get_meta_data(self):
		return self._meta_data

	def add_sensor(self, s):
		self._sensor_list.append(s)

	def connect(self, url, username, password):
		self._channel = mqpp_api.mqpp_api_connect(url, username, password)

	def push_data(self):
		message = {
			'api_key': self._api_key,
			'gateway_uuid': self._hub_uuid,
			'gateway_name': self._hub_name,
			'sensor_list': self._sensor_data_list
		}
		print json.dumps(message, sort_keys=True, indent=4)

		#url = '202.120.58.126'
		#username = 'admin'
		#password = 'omnilab'

		message_json = json.dumps(message)
		#channel = mqpp_api.mqpp_api_connect(url, username, password)
		mqpp_api.mqpp_api_publish(self._channel, message_json)
		#mqpp_api.mqpp_api(url, username, password, message_json)
		return True

	def parse_data(self):
		return True

	def pack_sensor_data(self):
		for s in self._sensor_list:
			sensor_data = {
				'sensor_uuid': s.get_sensor_uuid(),
				'sensor_name': s.get_sensor_name(),
				'sensor_type': s.get_sensor_type(),
				'sensor_value': s.get_sensor_value(),
				'sensor_unit': s.get_sensor_unit(),
				'datetime': s.get_datetime(),
				'longitude': s.get_longitude(),
				'latitude': s.get_latitude()
			}
			self._sensor_data_list.append(sensor_data)
		return True




		
