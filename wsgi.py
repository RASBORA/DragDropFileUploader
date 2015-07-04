#!D:\Python27\python.exe
# -*- coding: utf-8 -*-

import cgi

def application(environ, start_response):

    start_response("200 OK",[('Content-Type','text/html')])

    method = environ.get('REQUEST_METHOD')

    print_char =  '''
    	<meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\n
    	<div>WSGI PROGRAM</div>
    '''

    return print_char
