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
upload_folder = environment.upload_folder
os.chdir(upload_folder)

def application(environ, start_response):
	start_response("200 OK",[('Content-Type','text/html')])
	#method = environ.get('REQUEST_METHOD')
	picturelist =os.listdir(common.datadir)
	jsonbuff =[]
	for data in picturelist:
		jsonbuff.append({"url":common.datadir+data,"preview":common.datadir+data})

	json_char = json.dumps(jsonbuff)
	htmltext = json_char 
	return htmltext
