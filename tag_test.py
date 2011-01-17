#!/usr/bin/env python

from dedup import tags
mp3file = 'track1.mp3'
aacfile = 'track2.m4a'
print "comparing %s and %s:" % (mp3file, aacfile)
print "\t", tags.cmp_files(mp3file, aacfile)

mp3file = '/Volumes/Data/Music/Music/Zeromancer/Zzyzx/02 Hollywood.mp3'
aacfile = '/Volumes/Data/Music/Music/Zeromancer/Zzyzx/02 Hollywood.m4a'
print "comparing %s and %s:" % (mp3file, aacfile)
print "\t", tags.cmp_files(mp3file, aacfile)
