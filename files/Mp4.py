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
        self.artist     = self.aac['\xa9ART'][0]
        self.album      = self.aac['\xa9alb'][0]
        self.title      = self.aac['\xa9nam'][0]

    def __load_info(self):
        self.length     = self.aac.info.length
        self.bitrate    = self.aac.info.bitrate
