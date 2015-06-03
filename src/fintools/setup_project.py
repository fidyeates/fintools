#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
setup_project.py

Sets up a python project for you
"""

__version__ = 0.1
__author__  = "Fin"

# Stdlib Imports
import sys
import os

# Third Party Imports
import yaml

# Fin Imports

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

TEMPLATE_DIR = os.path.join(CURRENT_DIR, "templates")

TEMPLATE_MAP = {}
for fn in os.listdir(TEMPLATE_DIR):
    TEMPLATE_MAP[fn] = os.path.join(TEMPLATE_DIR, fn)

CONFIG = yaml.load(open(os.path.join(CURRENT_DIR, "project_layout.yaml"), 'r').read())

def create_files(sub_config, project_name, prefix):
    for filename in sub_config:
        fn = TEMPLATE_MAP.get(filename)
        if fn is None:
            print "Cant Find File: %s" % filename
            continue
        raw = ""
        with open(fn, 'r') as f:
            raw = f.read()
        raw = raw.replace("$NAME", project_name)
        fp = open(os.path.join(prefix, filename), 'wb')
        fp.write(raw)
        fp.close()


def create_structure(config, project_name, prefix=""):
    for folder_name, sub_config in config.items():
        if folder_name == "_files":
            create_files(sub_config, project_name, prefix)
            continue
        sub_prefix = os.path.join(prefix, folder_name)
        sub_prefix = sub_prefix.replace("$NAME", project_name)
        os.mkdir(sub_prefix)
        if sub_config is not None:
            create_structure(sub_config, project_name, sub_prefix)


def main():
    if len(sys.argv) < 3:
        print "Usage: python {} PROJECT_NAME PROJECT_DIR".format(sys.argv[0])
        exit(1)
    project_name = sys.argv[1]
    project_dir = sys.argv[2]
    prefix = os.path.join(project_dir, project_name)
    create_structure(CONFIG["root"], project_name, prefix)

if __name__ == '__main__':
    main()
