#!/usr/bin/python3
"""Creating deploy files"""
from fabric.api import local, put, run, env
import datetime

env.hosts = ['100.26.167.206', '100.26.161.102']


def do_pack():
    """Creating deploy files"""
    local('mkdir -p versions')
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_%s.tgz" % timestamp
    local('tar -cvzf "%s" ./web_static' % filename)
    return filename


def do_deploy(archive_path):
    """Creating deploy files"""
    try:
        file_name = archive_path.split("/")[-1]
        file_without = file_name.split(".")[0]
        dirname = "/data/web_static/releases/%s" % file_without

        put(archive_path, "/tmp")
        run("sudo mkdir -p %s" % dirname)
        run("sudo tar -xzf /tmp/%s -C %s" % (file_name, dirname))
        run("sudo rm /tmp/%s" % file_name)
        run("sudo mv %s/web_static/* %s/" % (dirname, dirname))
        run("sudo rm -rf %s/web_static" % dirname)
        run("rm -rf /data/web_static/current")
        run("sudo ln -s %s/ /data/web_static/current" % dirname)
        return True
    except Exception:
        return False
