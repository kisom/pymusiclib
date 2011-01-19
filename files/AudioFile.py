from Crypto.Hash import MD5 as Hasher
from sys import stderr
err = stderr.write

class AudioFile():
    
    file        = None
    artist      = None
    album       = None
    title       = None
    track       = None
    alb_tracks  = None
    disc        = None
    disc_set    = None
    year        = None
    fhash       = None
    length      = None
    bitrate     = None
    type        = None


    def __init__(self, filename, filehash = True):
        self.file = filename
        self.__load_tags()
        self.__load_info()
        if filehash: self.__load_hash()

    def __load_tags(self):
        pass

    def __load_info(self):
        pass

    def __load_hash(self):
        try:
            f   = open(self.file, 'r')
        except IOError, e:
            err('could not load hash for file %s!' % self.file)
            return
        else:
            self.fhash = Hasher.new(f.read()).digest()
            f.close() 

    def write_tags(self):
        pass

    def print_tags(self):
        if self.artist:
            print "Artist: %s" % self.artist
        if self.album:
            print "Album:  %s" % self.album
        if self.title:
            print "Title:  %s" % self.title
        if self.track: 
            print "Track", self.track, 
            if self.alb_tracks:
                print "/", self.alb_tracks
            else:
                print ""
        if self.disc:
            print "Disc", self.disc,
            if self.disc_set:
                print "/", self.disc_set
            else:
                print ""
        if self.year:
            print "Year:   %s" % self.year
        if self.length: 
            print "Length: %s sec" % self.length
        if self.bitrate:
            print "Bitrate: %d" % self.bitrate
        if self.type:
            print "Type:   %s" % self.type

