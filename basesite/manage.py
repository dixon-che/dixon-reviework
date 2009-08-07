#!/usr/bin/env python
import sys
from os import path

SITE_ROOT_DIR = path.split( path.dirname( path.abspath(sys.argv[0]) ) )[0] + '/'
sys.path.insert(0, SITE_ROOT_DIR)

from django.core.management import execute_manager

try:
    from basesite import settings
except ImportError:
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)
