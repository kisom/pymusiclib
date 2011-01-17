from Crypto.Hash import MD5 as Hasher
from sys import stderr
err = stderr.write

class AudioFile():
    
    file    = None
    artist  = None
    album   = None
    title   = None
    fhash   = None
    length  = None
    brate   = None


    def __init__(self, filename):
        self.file = filename
        self.__load_tags()
        self.__load_info()
        self.__load_hash()

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


