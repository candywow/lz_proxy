#! /usr/bin/env python
# -*- coding=UTF-8 -*-

'''
    start lizheng proxy application
    @author: Jieyi Wang
    @email: jiezhen@sjtu.edu.cn
'''
import config


class ProxyStart:
	def __init__(self, url, username, passord):
		self._url = url
		self._username = username
		self._passord = passord
		self._proxy = None

	def proxy_start(self):
		lizheng_config = config.ProxyConfig('lizheng_proxy.json')
		lizheng_config.load()
		self._proxy = lizheng_config.get_proxy()
		self._proxy.connect(self._url, self._username, self._passord)

	def proxy_publish(self, data=None):
		#self._proxy.set_meta_data(data)
		self._proxy.get_data()
		self._proxy.parse_data()
		self._proxy.pack_sensor_data()
		self._proxy.push_data()

#url = '202.120.58.126'
#username = 'admin'
#password = 'omnilab'
#proxy = ProxyStart(url, username, password)
#proxy.proxy_start()
#proxy.proxy_publish()