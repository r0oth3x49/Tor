#!/usr/bin/env python
import os

def check_path(filename):
    path,ext = filename.split('*')
    for dirpath, dirname, files in os.walk(path):
        for f in files:
            if f.endswith(ext):
                path = os.path.join(dirpath, f)
    return path
