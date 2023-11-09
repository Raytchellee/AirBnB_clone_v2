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
    """Deploys them to server"""
    if not os.path.isfile(archive_path):
        return False
    file = put(archive_path, "/tmp", use_sudo=True)
    route = re.compile(r"versions/(.+)\.tgz")
    f = route.search(archive_path).group(1)
    new_foldr = run("sudo mkdir -p /data/web_static/releases/{}/".
                    format(f))

    opened = run("sudo tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/".
                 format(f, f))
    delete_file = run("sudo rm /tmp/{}.tgz".format(f))

    mv_cmd = "sudo mv /data/web_static/releases/{}/web_static/*"
    path_name = "/data/web_static/releases/{}/"
    concat = mv_cmd + " " + path_name
    run_file = run(concat.format(f, f))

    del_path = run("sudo rm -rf /data/web_static/releases/{}/web_static".
                   format(f))
    del_link = run("sudo rm -rf /data/web_static/current")

    cr_link = ("sudo ln -s /data/web_static/releases/{}/ "
               "/data/web_static/current").format(f)
    new_link = run(cr_link)

    if all([file.succeeded, new_foldr.succeeded, opened.succeeded,
            delete_file.succeeded, run_file.succeeded,
            del_path.succeeded, del_link.succeeded, new_link.succeeded]):
        return True
    return False
