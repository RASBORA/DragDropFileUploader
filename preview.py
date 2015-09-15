#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path
import sys
import cgi
import json

#User Import
import common
import environment
os.chdir(environment.exec_folder)

def application(environ, start_response):

	#method = environ.get('REQUEST_METHOD')
	name = 'SCRIPT_NAME'
	info = 'PATH_INFO'

	scriptname = environ.get(name, '')
	pathinfo = environ.get(info, '')

	if(pathinfo.startswith("/preview.py") ):
		start_response("200 OK",[('Content-Type','text/html')])
		picturelist =os.listdir(common.datadir)
		jsonbuff =[]
		for data in picturelist:
			jsonbuff.append({"url":common.datadir+data,"preview":common.datadir+data})
		json_char = json.dumps(jsonbuff)
		htmltext = json_char
		return htmltext
	else:
		'''html = open("index.jpg","rb")
		header = [('Content-Type','image/jpeg'),('content-length', str(len(html)))]
		start_response("200 OK",header)
		page = html.read()'''
		html = open("preview.html","rb").read()
		header = [('Content-Type','text/html'),('content-length', str(len(html)))]
		start_response("200 OK",header)

	return html
