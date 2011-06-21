#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: amazon_scrub.py
# author: kyle isom <coder@kyleisom.net>
#
# removes tracking information from Amazon MP3s
import re
import sys
from mutagen import id3, mp3

def get_mp3(filename):
    try:
        f = open(filename)
    except IOError as e:
        return None
    else:
        f.close()
        return mp3.MP3(filename)

def scrub(audio):
    print '[+] scrubbing %s' % audio.filename
    cartel_tag = None

    for tag in audio.tags:
        if 'COMM' in tag:
            print '\t[+] scrubbing comment...'
            audio.tags[tag].text[0] = unicode(
                                      re.sub(r'Amazon.com Song ID: \d+', 
                                             '', audio.tags[tag].text[0]))
            if not audio.tags[tag].text[0]:
                audio.tags[tag].text[0] = 'Scrubbed by kisom\'s PyMusicLib.'

        if 'PRIV' in tag:
            print '\t[+] scrubbing cartel required metadata...'
            if 'amazon.com' in tag:
                cartel_tag = tag

    if cartel_tag:
        del audio.tags[cartel_tag]

    print '\t[+] saving...'
    audio.save()
    print '\t[+] done!'

def scrub_list(file_list):
    for f in file_list:
        a = get_mp3(f)
        scrub(a)

if __name__ == '__main__':
    files = sys.argv[1:]

    if not files:
        exit(1)

    scrub_list(sys.argv[1:])

        
