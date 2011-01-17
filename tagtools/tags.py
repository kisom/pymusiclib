#!/usr/bin/env python

import mp3tags
import mp4tags

tags = {
    'TITLE':'TIT2',
    'ALBUM':'TALB',
    'ARTIST':'TPE1'
}

def cmp_tags(file1_tags, file2_tags):
    tag_union = set.intersection(
        set(file1_tags.keys()),
        set(file2_tags.keys())
    )
    
    for tag in tag_union:
        if not file1_tags[tag] == file2_tags[tag]:
            return False
        
    return True

def cmp_files(file1, file2):
    
    # get tags for first file based on file type
    if mp3tags.is_mp3(file1):
        tags1 = mp3tags.get_tags(file1)
    elif mp4tags.is_mp4(file2):
        tags1 = mp4tags.get_tags(file1)
    else:
        return None
    
    # repeat for second file
    if mp3tags.is_mp3(file2):
        tags2 = mp3tags.get_tags(file2)
    elif mp4tags.is_mp4(file2):
        tags2 = mp4tags.get_tags(file2)
    else:
        return None
    
    return cmp_tags(tags1, tags2)


    