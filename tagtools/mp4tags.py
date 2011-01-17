#!/usr/bin/env python
# set of functions to work with mp4 tags

from mutagen import mp4

tag_trans = {
    'TITLE':'\xa9nam',
    'ALBUM':'\xa9alb',
    'ARTIST':'\xa9ART',
}

def cmp_tags(file1, file2):
    aac1 = mp4.MP4(file1)
    aac2 = mp4.MP4(file2)
    
    aac_tags = set.intersection(
        set(aac1.keys()),
        set(aac2.keys())
    )

    for tag in aac_tags:
        if not tag in tag_trans: continue
        if aac1[tag][0] != aac2[tag][0]:
            return False
    
    return True

def get_tags(file):
    """
    return a dictionary of tags and values using the tag_trans to translate
    tags to a standard that can be compared between file types.
    """
    aac = mp4.MP4(file)
    tags = { }
    
    for tag in tag_trans:
        tags[tag] = aac[tag_trans[tag]][0]
    
    return tags

def is_mp4(file):
    try:
        aac = mp4.MP4(file)
    except mp4.MP4StreamInfoError:
        return False
    else:
        return True

