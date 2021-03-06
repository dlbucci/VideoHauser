#!/usr/bin/python
import os, cgi
from convert import webm

# for email
import requests

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
    url = "/media/%s.webm" % str(id)
    embed_url = "http://videohauser-dlbucci.rhcloud.com/video/%s" % id
    return template('video', video_path=url, embed_path=embed_url)

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
    upload = request.files.get("video")
    if upload == None:
        redirect("/")
        return "None upload"

    random_name = ("%032x" % random.getrandbits(128))

    url = "/video/%s" % random_name
    
    name, ext = os.path.splitext(upload.filename)

    tmp_path = os.environ.get("OPENSHIFT_TMP_DIR")
    if tmp_path == None:
        tmp_path = './videos'
    
    save_path = os.environ.get("OPENSHIFT_DATA_DIR")
    if save_path == None:
        save_path = './videos'

    upload.filename = "%s%s" % (random_name, ext)
    upload.save(tmp_path) # appends upload.filename automatically
    
    # this function will remove the temporary video file
    webm(tmp_path, save_path, upload.filename)
    
    url = "/video/%s" % random_name
    
    # email the user with MailGun
    email = request.forms.get("email")
    if email:
        requests.post(
        "https://api.mailgun.net/v2/sandbox5fb6324798bc485184c48929dd535e92.mailgun.org/messages",
        auth=("api", "key-5pz3ehury2wexf8tubtmdurs4cvesur3"),
        data={"from": "Willy 'Video' Hauser <noreply@ssandbox5fb6324798bc485184c48929dd535e92.mailgun.org>",
              "to": [email],
              "subject": "Your New VideoHauser Link",
              "text": """\
Your video is now accessible at: http://videohauser-dlbucci.rhcloud.com%s""" % url})
    
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
    data_dir = os.environ.get("OPENSHIFT_DATA_DIR")
    if (data_dir):
        return static_file(path, root=data_dir, mimetype="video/webm")
    else:
        return static_file(path, root="./videos", mimetype="video/webm")
      
@route("/favicon.png")
def callback():
    repo_dir = os.environ.get("OPENSHIFT_REPO_DIR")
    if (repo_dir):
        return static_file("favicon.png", root=os.path.join(repo_dir, "static"))
    else:
        return static_file("favicon.png", root="./static")
  
@route("/robots.txt")
def callback():
    repo_dir = os.environ.get("OPENSHIFT_REPO_DIR")
    if (repo_dir):
        return static_file("robots.txt", root=os.path.join(repo_dir, "static"))
    else:
        return static_file("robots.txt", root="./static")

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

