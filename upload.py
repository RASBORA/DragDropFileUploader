#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import cgitb
import io
import os
import os.path
import sys
import hashlib
import traceback


#User Import
import common
import environment
upload_folder = environment.upload_folder
os.chdir(upload_folder)

print "upload.py START"

def application(environ, start_response):
    start_response("200 OK",[('Content-Type','text/html')])

    method = environ.get('REQUEST_METHOD')

    print_char = \
    '''
    	<meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\n
    	<div>UPLOADER</div>\n
    '''
    debug_char = os.getcwd() +"<br>"+str(os.listdir(os.getcwd()))

    if method == "POST":
        wsgi_input     = environ['wsgi.input']
        content_length = int(environ.get('CONTENT_LENGTH', 0))

        post_env = environ.copy()
        post_env['QUERY_STRING'] = ''
        try:
            form = cgi.FieldStorage(fp=wsgi_input,environ=post_env,keep_blank_values=True)
            #インスタンスが一つと想定
            post_data1 = form["file1"]
            if post_data1.file:
                if not os.path.isdir(upload_folder+common.datadir):
                    os.mkdir("data",0777)
                filehash = hashlib.sha256(post_data1.file.read())
                post_data1.file.seek(0)
                filename = filehash.hexdigest()
                #拡張子
                ext = os.path.splitext(post_data1.filename)[1]
                savefullpath = common.datadir+filename+ext
                if not os.path.isfile(savefullpath):
                    print_char += post_data1.filename
                    
                    fp = open(savefullpath,"wb")
                    fp.write(post_data1.file.read())
                    fp.close()
                else:
                    print_char += "this file uploaded"
            else:
                print_char += "not found files"
        except:
            print_char += "file upload failed"
            traceback.print_exc(file=sys.stdout)
        

    return print_char + "<br>PAGE END<br>" + debug_char
