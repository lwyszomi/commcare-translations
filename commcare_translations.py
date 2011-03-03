from os.path import join, normpath
import re
from StringIO import StringIO

def loads(s):
    # okay this is an abstraction violation, but I wrote load(f) so I know this will work
    f = s.split('\n')
    return load(f)
    
def load(f):
    messages = {}
    for line in f:
        line = re.split(r'(?<!\\)#', line)[0] # strip comments starting with '#', ignoring '\#'
        line = line.strip()
        if not line: continue
        i = line.index('=')
        messages[line[:i].strip()] = line[i+1:].strip()
    return messages

def load_translations(lang):
    path = normpath(join(__file__, '../messages_{lang}.txt'.format(lang=lang)))
    try:
        with open(path) as f:
            return load(f)
    except IOError:
        return {}

def dumps(dct):
    io = StringIO()
    for key,val in dct.items():
        print >> io, "{key}={val}".format(key=key, val=val)
    return io.getvalue()