from AudioFile import AudioFile
from mutagen import mp3
from mutagen import id3

class Mp3 (AudioFile):

    audio = None
    audio_encoding = { }

    def __init__(self, filename, filehash = True):
        AudioFile.__init__(self, filename, filehash)
        self.type = 'MPEG-3 audio stream'
        self.audio = mp3.MP3(self.file)
        self.__load_tags()
        self.__load_info()
        del self.audio

    
    def __load_tags(self):
        # load artist
        if 'TPE1' in self.audio.keys():
            self.artist     = self.audio['TPE1'][0]
            self.audio_encoding['artist'] = self.audio['TPE1'].encoding
        else:
            self.audio_encoding['artist'] = 0

        # load album
        if 'TALB' in self.audio.keys():
            self.album      = self.audio['TALB'][0]
            self.audio_encoding['album']  = self.audio['TALB'].encoding
        else:
            self.audio_encoding['album'] = 0

        # load title
        if 'TIT2' in self.audio.keys():
            self.title      = self.audio['TIT2'][0]
            self.audio_encoding['title']  = self.audio['TIT2'].encoding
        else:
            self.audio_encoding['title']  = 0

        # load track
        if 'TRCK' in self.audio.keys():
            (self.track, self.maxtracks) = self.audio['TRCK'][0].split('/')
            self.audio_encoding['tracks'] = self.audio['TRCK'].encoding
        else
             self.audio_encoding['tracks']  = 0
            

    def __load_info(self):
        self.length     = self.audio.info.length
        self.bitrate    = self.audio.info.bitrate

    def write_tags(self):
        self.audio = id3.ID3(self.file)

        # add tags

        audio.add(id3.TPE1(encoding = self.audio_encoding['artist'], 
                     text           = self.artist ))
        audio.add(id3.TALB(encoding = self.audio_encoding['album'], 
                     text           = self.album))
        audio.add(id3.TIT2(encoding = self.audio_encoding['title'],
                     text           = self.title))
        
        audio.save()
        
