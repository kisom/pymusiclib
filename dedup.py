#!/usr/bin/env python
# dedup.py
# python script to clear a music library of duplicates

import argparse
import datetime
import os
import pdb
import re
import sys
from files.MagicFile import MagicFile
from files import FileTools

num_removed = 0
debug       = False
readonly    = True
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
    LOG("[-] cwd: %s\n" % os.getcwd())
    files = os.listdir('.')
    
    # build file list
    for file in files:
        file_data[file] = { }
        file_data[file]['af']   = MagicFile(file)
        file_data[file]['dupe'] = False
    
    files = [f for f in files if not file_data[f]['af'] == None ]

    for curfile in files:
        if file_data[curfile]['dupe']: continue

        if debug:
            LOG('[-] current file: %s\n' % curfile)
            LOG('[-]\ttrack: %s\n' % FileTools.tag_str(
                file_data[curfile]['af']
            ))
            
        targets = [ f for f in files if not f == curfile ]

        for target in targets:
            if file_data[target]['dupe']: continue
            selected = FileTools.select(
                                file_data[curfile]['af'],
                                file_data[target]['af']
            )

            if selected:
                if debug:
                    LOG('[-] selecting with duplicate %s\n' % target)
                    LOG("[-]\t%s selected\n" % (selected, ))
                    
                file_data[selected]['dupe'] = True
        
    for file in files:
        if file_data[file]['dupe']:
            try:
                if not readonly: os.unlink(file)
            except:
                if debug:
                    LOG('[!] failed to remove %s/%s\n' % (path, file))
            else:
                removed.append(file)
                if debug:
                    LOG('[+] removed file %s/%s\n' % (path, file))
    
    return len(removed)

def tango(path):
    """
    dance through the file system
    """
    global num_removed
    
    if debug:
        LOG('attempting to walk %s\n' % path)
    
    os.chdir(path)
    cwd  = os.getcwd()
    tree    = os.walk(path)
    
    while True:
        if debug:
            LOG('currently in %s\n' % os.getcwd())
        try:
            (dirp, dirs, files) = tree.next()
        except:
            break
        else:
            if len(files) < 2: continue         # no point comparing 1 file
            num_removed += scan_dir(dirp)
            os.chdir(cwd)
        
    LOG('removed %d files\n' % num_removed)

def main(target):
    if debug:
        now = datetime.datetime.now()
        LOG('[+] starting dedup at %s\n' % str(now))
        if readonly:
            LOG('[+] _not_ removing files - readonly mode selected\n')
        
    tango(target)
    
    if debug:
        end = datetime.datetime.now()
        LOG('[+] finished dedup at %s\n' % str(end))
        delta = end - now
        LOG('[+] %d files removed in %s\n' % (num_removed, str(delta)))
    else:
        LOG('deleted %d files\n' % num_removed)

    
# main code
if '__main__' == __name__:
    
    aparser = argparse.ArgumentParser(description='python utility to remove '+
                                      'duplicates from a music library')
    aparser.add_argument('-d', '--debug', action = 'store_true',
                         help = 'enable debug / logging output')
    aparser.add_argument('-l', '--logfile', help = 'file to log to, defaults '+
                         'to stdout')
    aparser.add_argument('-r', '--readonly', action = 'store_true',
                         help = "only log what would be done, don't actually " +
                         "remove any files")
    aparser.add_argument('target', help = 'path to music library')
    args = aparser.parse_args()

    if args.debug:
        debug = True
    
    if args.readonly:
        readonly = True

    if args.logfile:
        setup_logger(args.logfile)
        
    main(args.target)