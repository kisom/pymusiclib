from AudioFile import AudioFile
from Mp3 import Mp3
from Mp4 import Mp4
from FileTools import get_extension

debug = False


def MagicFile(filename, filehash = True):
    # won't work if we ever get around to procession FLAC
    extension = get_extension(filename)

    if extension == 'mp3':
        return Mp3(filename, filehash)
    elif extension == 'm4a':
        return Mp4(filename, filehash)
    elif extension == 'mp4':
        return Mp4(filename, filehash)
    else:
        if debug: print 'invalid file!'
        return None


