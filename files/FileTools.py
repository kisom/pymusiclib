from AudioFile import AudioFile

def get_extension(filename):
    index = filename.rfind('.')
    if index == 0:
        return None
    return filename[index + 1:]

def compare_tags(af1, af2):
    if not af1.title  == af2.title:  return False
    if not af1.artist == af2.artist: return False
    if not af1.album  == af2.album:  return False
    return True

def compare_info(af1, af2):
    if not af1.length  == af2.length:  return False
    if not af1.bitrate == af2.bitrate: return False
    return True
    
def compare_hash(af1, af2):
    if not af1.fhash == af2.fhash: return False
    return True

def compare_files(af1, af2):
    if not compare_tags(af1, af2): return False
    if not compare_info(af1, af2): return False
    if not compare_hash(af1, af2): return False
    return True

def select_better(af1, af2):
    if af2.bitrate > af1.bitrate:     return af2.file   # prefer higher bitrate
    if len(af1.file) > len(af2.file): return af2.file   # prefer shorter
                                                        #   filenames
    return af1.file

def select_remove(af1, af2):
    """
    select which file should be removed
    """
    if af2.bitrate < af1.bitrate:     return af2.file   # prefer higher bitrate
    if len(af1.file) < len(af2.file): return af2.file   # prefer shorter
                                                        #   filenames
    return af1.file
def compare_types(af1, af2):
    if af1.type == af2.type: return True
    return False

def compare(af1, af2):
    if compare_types(af1, af2):
        return compare_files(af1, af2)
    else:
        return compare_tags(af1, af2) and compare_info(af1, af2)

def select(af1, af2):
    if compare(af1, af2):
        return select_remove(af1, af2)
    else:
        return False

def tag_str(af):
    tag = "%s - %s - %s" % (af.artist, af.album, af.title)

    return unicode.encode(tag, 'utf-8')
