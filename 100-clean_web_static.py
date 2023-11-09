#!/usr/bin/python3
# Deletes archive files
from fabric.api import *
import os

env.hosts = ['100.26.167.206', '100.26.161.102']


def do_clean(number=0):
    """Removes outdated archives"""
    if int(number) == 0:
        number = 1
    else:
        number = int(number)

    foldrs = sorted(os.listdir("versions"))
    [foldrs.pop() for _ in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(idx)) for idx in foldrs]

    with cd("/data/web_static/releases"):
        foldrs = run("ls -tr").split()
        foldrs = [idy for idy in foldrs if "web_static_" in idy]
        [foldrs.pop() for _ in range(number)]
        [run("rm -rf ./{}".format(idy)) for idy in foldrs]
