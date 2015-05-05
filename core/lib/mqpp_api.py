#! /usr/bin/env python
# -*- coding=UTF-8 -*-

'''
    API of Message Queue Producer
    @author: Bin Zhang
    @email: zhangbinsjtu@gmail.com
'''

import pika

def mqpp_api_connect(url, username, password):
    credentials = pika.PlainCredentials(username, password)
    parameters = pika.ConnectionParameters(url, 5672, '/', credentials)
    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()
    return channel

def mqpp_api_publish(channel, message):
    channel.basic_publish(exchange='exchange', routing_key='routing_key', body=message)
    print '[t] ' + message
