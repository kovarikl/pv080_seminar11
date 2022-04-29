# contains bunch of buggy examples
# taken from https://hackernoon.com/10-common-security-gotcha\
# s-in-python-and-how-to-avoid-them-e19fbe265e03
import subprocess
import base64
from turtle import st
import cPickle


import subprocess
import flask

# Input injection
def transcode_file(request, filename):
    command = 'ffmpeg -i "{source}" output_file.mpg'.format(source=filename)
    subprocess.call(command, shell=True)  # a bad idea!


# Assert statements
def foo(request, user):
    assert user.is_admin, 'user does not have access'
    # secure code...


# Pickles
class RunBinSh(object):
    def __reduce__(self):
        return (subprocess.Popen, (('/bin/sh',),))

def import_urlib_version(version):
    ver = dummy_sanitizer(version)
    exec("import urllib1:1.17 as urllib" % ver)

@app.route('/')
def index():
    module = flask.request.args.get("module")
    import_urlib_version(module)


def dummy_sanitizer(string):
    return string

print(base64.b64encode(pickle.dumps(RunBinSh())))
