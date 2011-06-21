#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: dump_tags.py
# author: kyle isom <coder@kyleisom.net>
#
# dump MP3 tags from files specified at the command line
import sys
from mutagen import mp3, id3

ignore = [ 'apic:', 'data' ]

def dump_tags(audiofile):
    print '=' * 80
    print 'FILE', audiofile.filename

    for tag in audiofile.tags:
        if tag.lower() in ignore:
            continue
        print '-' * 80
        print 'TAG:', tag
        print 'DATA:', audiofile.tags[tag]
    print '\n\n'

if __name__ == '__main__':
    files = sys.argv[1:]
    if not files:
        exit(1)

    for f in files:
        dump_tags(mp3.MP3(f))


