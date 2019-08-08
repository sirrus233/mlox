"""Handle program wide resources (files, images, etc...)"""
import os
import sys
import base64
import tempfile

import pkg_resources


def unpack_resource(data):
    """Convert base64 encoded data into a file handle, and a temporary file name to access the data"""
    file_handle = tempfile.NamedTemporaryFile()
    file_handle.write(base64.b64decode(data))
    file_handle.seek(0)
    return (file_handle,file_handle.name)


# Paths to resource files
program_path     = os.path.realpath(sys.path[0])
try:
    import appdirs
    user_path = appdirs.user_data_dir('mlox', 'mlox')
    if not os.path.isdir(user_path):
        os.makedirs(user_path)
except ImportError:
    user_path = program_path

resource_manager = pkg_resources.ResourceManager()

gif_file = resource_manager.resource_filename("mlox.static", "mlox.gif")
qml_file = resource_manager.resource_filename("mlox.static", "window.qml")
base_file = os.path.join(user_path, "mlox_base.txt")
user_file = os.path.join(user_path, "mlox_user.txt")

#For the updater
UPDATE_BASE      = "mlox-data.7z"
update_file      = os.path.join(user_path,UPDATE_BASE)
UPDATE_URL       = 'https://svn.code.sf.net/p/mlox/code/trunk/downloads/' + UPDATE_BASE
