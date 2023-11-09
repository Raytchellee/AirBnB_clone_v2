#!/usr/bin/python3
"""Creates archive file on both servers"""
import re
import datetime
from os import path
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
    if path.exists(archive_path):
        arch_path = archive_path.split('/')[1]
        arch_route = "/tmp/{}".format(arch_path)
        file_flder = arch_path.split('.')[0]
        file_route = "/data/web_static/releases/{}/".format(file_flder)

        put(archive_path, arch_route)
        run("mkdir -p {}".format(file_route))
        run("tar -xzf {} -C {}".format(arch_route, file_route))

        run("rm {}".format(arch_route))
        run("mv -f {}web_static/* {}".format(file_route, file_route))
        run("rm -rf {}web_static".format(file_route))
        run("rm -rf /data/web_static/current")

        run("ln -s {} /data/web_static/current".format(file_route))
        return True
    return False
