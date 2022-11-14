#!/usr/bin/python3
""" Function that compress a folder """
import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run


env.hosts = ['54.158.198.144', '54.237.35.160']
env.user = "ubuntu"

def do_deploy(archive_path):
    """Distributes an archive to a web server.
    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True

# def do_deploy(archive_path):
#     """Deploys the static files to the host servers.
#     Args:
#         archive_path (str): The path to the archived static files.
#     """
#     if not os.path.exists(archive_path):
#         return False
#     file_name = os.path.basename(archive_path)
#     folder_name = file_name.replace(".tgz", "")
#     folder_path = "/data/web_static/releases/{}/".format(folder_name)
#     success = False
#     try:
#         put(archive_path, "/tmp/{}".format(file_name))
#         run("mkdir -p {}".format(folder_path))
#         run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
#         run("rm -rf /tmp/{}".format(file_name))
#         run("mv {}web_static/* {}".format(folder_path, folder_path))
#         run("rm -rf {}web_static".format(folder_path))
#         run("rm -rf /data/web_static/current")
#         run("ln -s {} /data/web_static/current".format(folder_path))
#         print('New version deployed!')
#         success = True
#     except Exception:
#         success = False
#     return success
