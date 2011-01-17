from AudioFile import AudioFile
from mutagen import mp3

class Mp3 (AudioFile):

    id3 = None

    def __init__(self, filename, filehash = True):
        AudioFile.__init__(self, filename, filehash)
        self.type = 'MPEG-3 audio stream'
        self.id3 = mp3.MP3(self.file)
        self.__load_tags()
        self.__load_info()
        del self.id3

    
    def __load_tags(self):
        self.artist     = self.id3['TPE1'][0]
        self.album      = self.id3['TALB'][0]
        self.title      = self.id3['TIT2'][0]

    def __load_info(self):
        self.length     = self.id3.info.length
        self.bitrate    = self.id3.info.bitrate

