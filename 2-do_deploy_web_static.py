#!/usr/bin/python3
"""Module that generates a .tgz archive """
from fabric.api import local, put, run, env
from datetime import datetime
from os.path import exists

env.hosts = ['35.237.150.134', '35.185.50.255']


def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    format_date = datetime.now()
    format_date = format_date.strftime('%Y%m%d%H%M%S')
    filename = 'versions/web_static_{}.tgz'.format(format_date)
    local('mkdir -p versions', capture=True)
    tgz = local('tar -cvzf %s web_static' % filename)
    if tgz.succeeded:
        return filename
    else:
        return None


def do_deploy(archive_path):
    """deploy and uncompress file to server."""
    if not exists(archive_path):
        return False

    put(archive_path, "/tmp/")
    namefile = archive_path.split('/')[-1]
    name = namefile.split('.')[0]  # name withouth extension.
    pathfile = "/data/web_static/releases/" + name
    run("mkdir -p " + pathfile)
    run("tar -xzf /tmp/" + namefile + " -C " + pathfile)
    run("rm /tmp/" + namefile)

    run("mv " + pathfile + "/web_static/* " + pathfile)
    run("rm -rf " + pathfile + "/web_static/")
    run("rm -rf /data/web_static/current")
    run("ln -s {} /data/web_static/current".format(pathfile))
    return True
