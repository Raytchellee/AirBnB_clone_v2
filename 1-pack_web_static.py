#!/usr/bin/python3
""" Uses content of web_static to generate archive files"""
import datetime
from fabric.api import local


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
