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
    """distributes an archive to your web servers"""
    if not exists(archive_path):
        return False
    put(archive_path, "/tmp/")
    tx1 = archive_path.split('/')[-1]
    tx2 = tx1.split('.')[0]
    path = '/data/web_static/releases/' + tx2
    run('mkdir -p ' + path)
    st = 'tar -xzf /tmp/{} -C {}'.format(tx1, path)
    run(st)
    run('rm /tmp/' + tx1)
    run('mv {}web_static/* {}'.format(path, path))
    run('rm -rf {}web_static/*'.format(path))
    run('rm -rf /data/web_static/current')
    run('ln -s {} /data/web_static/current'.format(path))
