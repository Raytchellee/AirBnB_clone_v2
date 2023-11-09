#!/usr/bin/python3
"""Creates archive file on both servers"""
import re
import os.path
import datetime
from fabric.api import *

env.hosts = ['100.26.167.206', '100.26.161.102']


@runs_once
def do_pack():
    """Creates archive files"""
    try:
        local('mkdir -p versions')
        curr_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        local('tar -cvzf "versions/web_static_{}.tgz" ./web_static'.
              format(curr_time), capture=True)
        return "versions/web_static_{}.tgz".format(curr_time)
    except Exception as e:
        print(e)
        return None


def do_deploy(archive_path):
    """ deploys them to server """
    try:
        curr_file = archive_path.split("/")[-1]
        folder = curr_file.split(".")[0]
        path = "/data/web_static/releases/%s" % folder

        put(archive_path, "/tmp")
        run("sudo mkdir -p %s" % path)
        run("sudo tar -xzf /tmp/%s -C %s" % (curr_file, path))
        run("sudo rm /tmp/%s" % curr_file)
        run("sudo mv %s/web_static/* %s/" % (path, path))
        run("sudo rm -rf %s/web_static" % path)
        run("rm -rf /data/web_static/current")
        run("sudo ln -s %s/ /data/web_static/current" % path)
        return True
    except Exception:
        return False
