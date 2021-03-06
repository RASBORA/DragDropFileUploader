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

            if not os.path.isdir(upload_folder+common.datadir):
                os.mkdir("data",0777)

            file1 = form["file1"]
            if isinstance(file1, list):
                #file1の[0]に変なの入ってるぽい
                for f in file1[1:]:
                    print_char += writeFile(f)
            else:
                print_char += writeFile(file1)
        except:
            print_char += "file upload failed<br>"
            traceback.print_exc(file=sys.stdout)
        

    return print_char + "<br>PAGE END<br>" + debug_char

def writeFile(filehandle):
    if filehandle.file:
        filehash = hashlib.sha256(filehandle.file.read())
        filehandle.file.seek(0)
        filename = filehash.hexdigest()
        #拡張子
        ext = os.path.splitext(filehandle.filename)[1]
        savefullpath = common.datadir+filename+ext
        if not os.path.isfile(savefullpath):
            #print_char += filehandle.filename       
            fp = open(savefullpath,"wb")
            fp.write(filehandle.file.read())
            fp.close()
            return filehandle.filename+" - success<br>"
        else:
            return filehandle.filename+" - file exist<br>"
    else:
        return "not contain files<br>"
