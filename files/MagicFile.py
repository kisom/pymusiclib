from AudioFile import AudioFile
from Mp3 import Mp3
from Mp4 import Mp4

def MagicFile(filename):
    # won't work if we ever get around to procession FLAC
    extension = filename[-4:]

    if not extension[0] == '.':
        print 'invalid file!'
        return None

    extension = extension[1:]
    if extension == 'mp3':
        return Mp3(filename)
    elif extension == 'm4a':
        return Mp4(filename)
    elif extension == 'mp4':
        return Mp4(filename)
    else:
        print 'invalid file!'
        return None


