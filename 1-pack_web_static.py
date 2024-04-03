#!/usr/bin/python3
""" Fabric script that generates a .tgz archive """

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """ generates a .tgz archive from the contents""" \
            """of the web_static folder"""

    now = datetime.now().strftime("%Y%m%d%H%M%S")

    if not os.path.exists("versions"):
        os.makedirs("versions")

    archive_name = "web_static_" + now + ".tgz"

    result = local("tar -czvf versions/{} web_static".format(archive_name))

    if result.succeeded:
        return "version/" + archive_name
    else:
        return None
