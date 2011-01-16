#!/usr/bin/env python

import os
import sys
import ID3
import eyeD3

def valid_tags(id3):
    if len(id3.keys()) == 1:
        return False
    return True

def view_tags(file):
    print file
    id3info = ID3.ID3(file)
    if valid_tags(id3info):
        print "\tartist: %s" % id3info.artist
        print "\talbum: %s" % id3info.album
        print "\ttitle: %s" % id3info.title
        print


def check_tags(files):
    for file in files:
        if eyeD3.isMp3File(file):
            view_tags(file)

def check_dir(mp3dir):
    files = os.listdir(mp3dir)
    for file in files:
        file = "%s/%s" % (mp3dir, file)
        view_tags(file)
        

if "__main__" == __name__:
    if len(sys.argv) < 2:
        mp3dir = '.'
    else:
        mp3dir = sys.argv[1]

    check_dir(mp3dir)
