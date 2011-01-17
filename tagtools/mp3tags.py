#!/usr/bin/env python
from mutagen import mp3
from mutagen import id3

tag_chk = [ 'TPE2', 'TALB', 'TIT1' ]
tag_ignore = [ u'APIC:', u"COMM::'eng'", 'TDRC' ]
tag_trans = {
    'TITLE':'TIT2',
    'ARTIST':'TPE1',
    'ALBUM':'TALB',
}

def cmptags(file1, file2):
    id3inf1 = mp3.MP3(file1)
    id3inf2 = mp3.MP3(file2)

    tagset = set.intersection(
        set(id3inf1.keys()),
        set(id3inf2.keys())
    )

    for tag in tagset:
        if tag in tag_ignore: continue
        if not tag in tag_chk: continue
        if not id3inf1[tag][0] == id3inf2[tag][0]:
            print tag
            print "\t%s" % id3inf1[tag]
            print "\t%s" % id3inf2[tag]
            return False

    return True

def get_tags(file):
    id3 = mp3.MP3(file)
    tags = { }
    
    for tag in tag_trans:
        tags[tag] = id3[tag_trans[tag]][0]
    
    return tags

def is_mp3(file):
    try:
        id3 = mp3.MP3(file)
    except mp3.HeaderNotFoundError:
        return False
    else:
        return True
