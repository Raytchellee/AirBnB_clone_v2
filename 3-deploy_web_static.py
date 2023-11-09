#!/usr/bin/python3
"""creates archive file on both servers"""
import re
import os.path
import datetime
from fabric.api import *

env.hosts = ['100.26.167.206', '100.26.161.102']


@runs_once
def do_pack():
    """ creates archive files """
    try:
        local('mkdir -p versions')
        curr_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        local('tar -cvzf "versions/web_static_{}.tgz" ./web_static'.
              format(curr_time), capture=True)
        return "versions/web_static_{}.tgz".format(curr_time)
    except:
        return None


def do_deploy(archive_path):
    """ deploys them to server """
    try:
        curr_file = archive_path.split("/")[-1]
        fd_name = curr_file.split(".")[0]
        cur_path = "/data/web_static/releases/%s" % fd_name

        put(archive_path, "/tmp")
        run("sudo mkdir -p %s" % cur_path)
        run("sudo tar -xzf /tmp/%s -C %s" % (curr_file, cur_path))
        run("sudo rm /tmp/%s" % curr_file)
        run("sudo mv %s/web_static/* %s/" % (cur_path, cur_path))
        run("sudo rm -rf %s/web_static" % cur_path)
        run("rm -rf /data/web_static/current")
        run("sudo ln -s %s/ /data/web_static/current" % cur_path)
        return True
    except Exception:
        return False


def deploy():
    """ runs both commands"""
    file_path = do_pack()
    print(file_path)
    if file_path is None:
        return False

    return do_deploy(file_path)
