#!/usr/bin/python
import os, cgi

try:
    virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
    virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass
except:
    pass

#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#

import subprocess
import random

from bottle import route, template

@route("/")
def index():
    return template('templates/index')

@route("/health")
def health():
    return "1"

@route("/env")
def env():
    response_body = ['%s: %s' % (key, value)
                for key, value in sorted(environ.items())]
    response_body = '\n'.join(response_body)
    return response_body

@route("/upload", method="POST")
def upload():
    form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ, keep_blank_values=True)

    response_body = str(form)      

    try:
        fileitem = form['file']

        random_name = ("%032x" % random.getrandbits(128))

        response_body += "believed it was a file"
        fn = os.environ['OPENSHIFT_DATA_DIR'] + random_name + ".unenc"
        with open(fn, 'wb') as f:
            data = fileitem.file.read(1024)
            while data:
                f.write(data)
                data = fileitem.file.read(1024)

        f.close()

        '''try:
            out = os.environ['OPENSHIFT_DATA_DIR'] + random_name + ".webm"
            command = (os.environ["OPENSHIFT_BUILD_DEPENDENCIES_DIR"]+"ffmpeg -i "
                      + fn + " -c:v libvpx -b:v 0.5M -c:a libvorbis " + out)
            response_body += command
            response_body += subprocess.check_call(command)
            response_body += 'The file "' + fn + '" was uploaded successfully'
            command = "rm " + fn
            response_body += command
            response_body += subprocess.check_call(command)

        except subprocess.CalledProcessError, e:
            try:
                command = "rm "+fn
                response_body += command
                response_body += subprocess.check_call(command)
            except:
                pass
            response_body += str(e.output)
            repsonse_body += "Video encoding failed."
        except Exception, e:
            response_body += str(e)
            response_body += "Oh no! things must have gone terribly wrong."'''

    except KeyError:
        fileitem = None
        response_body += "Please upload a valid file"
    return response_body

#
# Below for testing only
#
if __name__ == '__main__':
    from bottle import run
    run(host="localhost", port=8051)
