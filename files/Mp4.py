from AudioFile import AudioFile
from mutagen import mp4

class Mp4 (AudioFile):
    """
    Load an standard AudioFile with MP4 information. Pass in a filename.
    """
    aac = None

    def __init__(self, filename, filehash = True):
        AudioFile.__init__(self, filename, filehash)
        self.type   = 'MPEG-4 audio stream'
        self.aac    = mp4.MP4(filename)
        self.__load_tags()
        self.__load_info()
        del self.aac

    def __load_tags(self):
        if '\xa9ART' in self.aac.keys():
            self.artist     = self.aac['\xa9ART'][0]
        if '\xa9alb' in self.aac.keys():
            self.album      = self.aac['\xa9alb'][0]
        if '\xa9nam' in self.aac.keys():
            self.title      = self.aac['\xa9nam'][0]
        if 'trkn' in self.aac.keys():
            (self.track, self.alb_tracks) = self.aac['trkn'][0]
        if 'disk' in self.aac.keys():
            (self.disc, self.disc_set)    = self.aac['disk'][0]
        if '\xa9day' in self.aac.keys():
            self.year       = self.aac['\xa9day'][0]

    def __load_info(self):
        self.length     = self.aac.info.length
        self.bitrate    = self.aac.info.bitrate

    def write_tags(self):
        
        self.aac = mp4.MP4(self.file)

        if self.artist:
            self.aac['\xa9ART'] = [ unicode(self.artist) ]
        if self.album:
            self.aac['\xa9alb'] = [ unicode(self.album) ]
        if self.title:
            self.aac['\xa9nam'] = [ unicode(self.title) ]

        if self.track:
            if self.alb_tracks:
                self.aac['trkn'] = [ (self.track, self.alb_tracks) ]
            else:
                self.aac['trkn'] = [ (self.track, 0) ]
        elif self.alb_tracks:
            self.aac['trkn']    = [ (0, self.alb_tracks) ]

        if self.disc:
            if self.disc_set:
                self.aac['disc'] = [ (self.disc, self.disc_set) ]
            else:
                self.aac['disc'] = [ (self.disc, 0) ]
        elif self.disc_set:
            self.aac['disc']    = [ (0, self.disc_set) ]

        if self.year:
            self.aac['\xa9day'] = [ unicode(self.year) ]

        self.aac.save()

        del self.aac
