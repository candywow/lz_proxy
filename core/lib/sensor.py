#! /usr/bin/env python
# -*- coding=UTF-8 -*-

'''
    class of sensor
    @author: Jieyi Wang
    @email: jiezhen@sjtu.edu.cn
'''

class sensor:

	def __init__(self, sensor_uuid, sensor_name, sensor_type, sensor_unit):
		self.sensor_uuid = sensor_uuid
		self.sensor_name = sensor_name
		self.sensor_type = sensor_type
		self.sensor_unit = sensor_unit
		self.sensor_value = None
		self.datetime = None
		self.longitude = None
		self.latitude = None

	def get_sensor_name(self):
		return self.sensor_name

	def get_sensor_uuid(self):
		return self.sensor_uuid

	def get_sensor_type(self):
		return self.sensor_type

	def get_sensor_unit(self):
		return self.sensor_unit

	def set_sensor_value(self, value):
		self.sensor_value = value

	def get_sensor_value(self):
		return self.sensor_value

	def set_datetime(self, datetime):
		self.datetime = datetime

	def get_datetime(self):
		return self.datetime

	def set_longitude (self, longitude):
		self.longitude  = longitude

	def get_longitude(self):
		return self.longitude

	def set_latitude(self, latitude):
		self.latitude = latitude

	def get_latitude(self):
		return self.latitude

