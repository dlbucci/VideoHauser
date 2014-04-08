#!/usr/bin/python
import os, cgi

virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass
#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#

import subprocess
import random

def application(environ, start_response):

    ctype = 'text/plain'
    if environ['PATH_INFO'] == '/health':
        response_body = "1"
    elif environ['PATH_INFO'] == '/env':
        response_body = ['%s: %s' % (key, value)
                    for key, value in sorted(environ.items())]
        response_body = '\n'.join(response_body)
    elif environ['PATH_INFO'] == '/upload' and environ['REQUEST_METHOD'] == 'POST':
      form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ, keep_blank_values=True)

      response_body = str(form)      

      try:
        fileitem = form['file']

        response_body += "believed it was a file"
        fn = os.environ['OPENSHIFT_DATA_DIR'] + os.path.basename(fileitem.filename)
        with open(fn, 'wb') as f:
          data = fileitem.file.read(1024)
          while data:
            f.write(data)
            data = fileitem.file.read(1024)

          try:
            out = os.environ['OPENSHIFT_DATA_DIR'] + ("%032x.webm" % random.getrandbits(128))
            command = os.environ["OPENSHIFT_BUILD_DEPENDENCIES_DIR"]+"ffmpeg -i "
                      + fn + " -c:v libvpx -b:v 0.5M -c:a libvorbis " + out
            response_body += command
            response_body += subprocess.check_call(command)
            response_body += 'The file "' + fn + '" was uploaded successfully'
            command = "rm "+fn
            response_body += command
            response_body += subprocess.check_call(command)

          except Exception, e:
            try:
              command = "rm "+fn
              response_body += command
              response_body += subprocess.check_call(command)
            except:
              pass
            response_body += str(e.output)
            repsonse_body += "Video encoding failed."

      except KeyError:
        fileitem = None
        response_body += "Please upload a valid file"

    else:
        ctype = 'text/html'
        response_body = '''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  <title>Welcome to VideoHauser</title>
</head>
<body>
Welcome to Video-Hauser
<form action="upload" method="post"
enctype="multipart/form-data">
<label for="file">Video to upload:</label>
<input type="file" name="file" id="file"><br>
<input type="submit" name="submit" value="Submit">
</form>
</body>
</html>'''
        

    status = '200 OK'
    response_headers = [('Content-Type', ctype), ('Content-Length', str(len(response_body)))]
    #
    start_response(status, response_headers)
    return [response_body]

#
# Below for testing only
#
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 8051, application)
    # Wait for a single request, serve it and quit.
    httpd.handle_request()
