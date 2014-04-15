#!/usr/bin/python
import os, cgi

try:
    virtenv = os.path.join(os.environ['OPENSHIFT_PYTHON_DIR'], 'virtenv')
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

from bottle import default_app, redirect, request, route, static_file, template

@route("/")
def index():
    return template('index')
  
@route("/video/<id>")
def video(id):
    url = "/media/%s.mp4" % str(id)
    return template('video', video_path=url)

@route("/health")
def health():
    return "1"

@route("/env")
def env():
    response_body = ['%s: %s' % (key, value)
                for key, value in sorted(request.environ.items())]
    response_body = '\n'.join(response_body)
    return response_body

@route("/upload", method="POST")
def upload_video():
    upload = request.files.get('video')
    if upload == None:
        redirect("/")
        return "None upload"

    random_name = ("%032x" % random.getrandbits(128))

    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.mp4', '.mpeg4'):
        return 'File extension not allowed.'

    save_path = os.environ.get("OPENSHIFT_DATA_DIR")
    if save_path == None:
        save_path = 'videos/'

    upload.filename = "%s.mp4" % random_name
    upload.save(save_path) # appends upload.filename automatically
    url = "/video/%s" % random_name
    redirect(url)

#
# this route serves static JS files
#
@route("/scripts/<path:path>")
def callback(path):
    repo_dir = os.environ.get("OPENSHIFT_REPO_DIR")
    if (repo_dir):
        return static_file(path, root=os.path.join(repo_dir, "scripts"))
    else:
        return static_file(path, root="./scripts")

@route("/media/<path:path>")
def callback(path):
    repo_dir = os.environ.get("OPENSHIFT_REPO_DIR")
    if (repo_dir):
        return static_file(path, root=os.path.join(repo_dir, "videos"), mimetype='video/mp4')
    else:
        return static_file(path, root="./videos")
    
#
# Below for testing only
#
if __name__ == '__main__':
    from bottle import run, TEMPLATE_PATH
    TEMPLATE_PATH.append("./templates/")
    run(host="localhost", port=8051, debug=True)
else:
    from bottle import TEMPLATE_PATH
    TEMPLATE_PATH.append(os.path.join(os.environ.get("OPENSHIFT_REPO_DIR"), "templates/"))
    application = default_app()

