#!/usr/bin/python3
"""Module that generates a .tgz archive """
from fabric.api import local
from datetime import datetime


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
