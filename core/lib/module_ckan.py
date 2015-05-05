#! /usr/bin/env python
# -*- coding=UTF-8 -*-

'''
    class of LiZhengProxy
    @author: Jieyi Wang
    @email: jiezhen@sjtu.edu.cn
'''

import urllib
import urllib2
import json

class ckan:

	def __init__(self,server_address,api_key,resource_id):
		self.server_address = server_address
		self.api_key = api_key
		self.resource_id = resource_id

	def create_datastore(self,fields):
		resource_dict = {
    		'resource_id': self.resource_id,
    		'force': True,
    		'fields':fields
    		# 'fields': [{'id': 'temperature', 'type':'float'},{'id': 'humidity', 'type': 'float'},{'id': 'pm25', 'type': 'float'}],
   		}
		data_dict = urllib.quote(json.dumps(resource_dict))

		request = urllib2.Request(self.server_address + '/api/3/action/datastore_create')
		request.add_header('Authorization', self.api_key)

		response = urllib2.urlopen(request, data_dict, timeout = 10)

		print response.read()

	def delete_datastore(self):
		resource_dict = {
    		'resource_id': self.resource_id,
    		'force': True,
   		}
		data_dict = urllib.quote(json.dumps(resource_dict))

		request = urllib2.Request(self.server_address + '/api/3/action/datastore_delete')
		request.add_header('Authorization', self.api_key)

		response = urllib2.urlopen(request, data_dict, timeout = 10)

		print response.read()

	def update_resource(self):
		resource_dict = {
    		'id': self.resource_id,
        	'url': self.server_address + '/datastore/dump/' + self.resource_id
   		}
		data_dict = urllib.quote(json.dumps(resource_dict))

		request = urllib2.Request(self.server_address + '/api/3/action/resource_update')
		request.add_header('Authorization', self.api_key)

		response = urllib2.urlopen(request, data_dict, timeout = 10)

		print response.read()

	def get_data(self,limit,offset):
		resource_dict = {
			'resource_id': self.resource_id,
			'limit': limit,
			'offset' :offset,
			'sort': '_id asc'
		}

		data_dict = urllib.quote(json.dumps(resource_dict))

		request = urllib2.Request(self.server_address + '/api/3/action/datastore_search')
		request.add_header('Authorization', self.api_key)

		response = urllib2.urlopen(request, data_dict, timeout = 10)
		response_dict = json.loads(response.read())

		#print response_dict['result']
		return response_dict['result']['records']

	def push_data(self,data):
		resource_dict = {
    		'resource_id': self.resource_id,
          	'force': True,
            'records': [data],
          	'method': 'insert',
    	}
   		
		data_dict = urllib.quote(json.dumps(resource_dict))

		request = urllib2.Request(self.server_address + '/api/3/action/datastore_upsert')
		request.add_header('Authorization', self.api_key)

		response = urllib2.urlopen(request, data_dict, timeout = 10)

		print response.read()

	def delete_data(self,filters):
		resource_dict = {
    		'resource_id': self.resource_id,
    		'force': True,
    		'filters': filters
   		}
		data_dict = urllib.quote(json.dumps(resource_dict))

		request = urllib2.Request(self.server_address + '/api/3/action/datastore_delete')
		request.add_header('Authorization', self.api_key)

		response = urllib2.urlopen(request, data_dict, timeout = 10)

		print response.read()


