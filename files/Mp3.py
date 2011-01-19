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
            (self.track, self.alb_tracks) = self.audio['TRCK'][0].split('/')
            self.audio_encoding['tracks'] = self.audio['TRCK'].encoding
        else:
             self.audio_encoding['tracks']  = 0

        # load disc
        if 'TPOS' in self.audio.keys():
            (self.disc, self.disc_set) = self.audio['TPOS'][0].split('/')
            self.audio_encoding['disc'] = self.audio['TPOS'].encoding
        else:
            self.audio_encoding['disc'] = 0

        # load year
        if 'TDRC' in self.audio.keys():
            self.year       = self.audio['TDRC'][0]
            self.audio_encoding['year'] = 0
        else:
            self.audio_encoding['year'] = 0
            

    def __load_info(self):
        self.length     = self.audio.info.length
        self.bitrate    = self.audio.info.bitrate

    def write_tags(self):
        self.audio  = id3.ID3(self.file)
        tracks      = u'%s/%s' % (unicode(self.track), 
                                  unicode(self.alb_tracks))
        disc        = u'%s/%s' % (unicode(self.disc), unicode(self.disc_set))
        # add tags

        self.audio.add(id3.TPE1(encoding = self.audio_encoding['artist'], 
                     text                = unicode(self.artist )))
        self.audio.add(id3.TALB(encoding = self.audio_encoding['album'], 
                     text                = unicode(self.album)))
        self.audio.add(id3.TIT2(encoding = self.audio_encoding['title'],
                     text                = unicode(self.title)))
        self.audio.add(id3.TRCK(encoding = self.audio_encoding['tracks'],
                     text                = tracks))
        self.audio.add(id3.TPOS(encoding = self.audio_encoding['disc'],
                     text                = disc))
        self.audio.add(id3.TDRC(encoding = self.audio_encoding['year'],
                     text                = unicode(self.year)))

        
        self.audio.save()
        
