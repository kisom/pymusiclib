#!/usr/bin/env python
# dedup.py
# python script to clear a music library of duplicates

import os
import pdb
import re
import sys
from files.MagicFile import MagicFile
from files import FileTools

num_removed = 0
debug       = False
LOG         = sys.stdout.write
LOGF        = None

def setup_logger(logfile):
    global LOG
    global LOGF
    
    try:
        LOGF = open(logfile, 'a')
    except IOError, e:
        print e
        sys.exit(1)
    else:
        LOG = LOGF.write


def scan_dir(path):
    file_data   = { }
    removed     = [ ]
    dupes       = [ ]
    os.chdir(path)
    files = os.listdir('.')
    
    # build file list
    for file in files:
        file_data[file] = { }
        file_data[file]['af']   = MagicFile(file)
        file_data[file]['dupe'] = False

    for curfile in files:
        if file_data[curfile]['dupe']: continue

        if debug:
            LOG('current file: %s' % curfile)
            LOG('track: %s' % FileTools.tag_str(file_data['af']))
            
        targets = [ f for f in files if not f == curfile ]

        for target in targets:
            if file_data[target]['dupe']: continue
            selected = FileTools.select(
                                file_data[curfile]['af'],
                                file_data[target]['af']
            )

            if selected:
                if debug:
                    LOG("[-]\t%s selected" % (selected, ))
                    
                file_data[selected]['dupe'] = True
        
    for file in files:
        if file_data[file]['dupe']:
            try:
                os.unlink(file)
            except:
                LOG('[!] failed to remove %s/%s' % (path, file))
            else:
                removed.append(file)
                LOG('[+] removed file %s/%s' % (path, file))
    
    return len(removed)

def tango(path):
    """
    dance through the file system
    """
    popcwd  = os.getcwd()
    tree    = os.walk(path)
    
    while True:
        try:
            (cwd, dirs, files) = tree.next()
        except:
            break
    
