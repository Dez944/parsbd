import re
import string

nonprintable = re.compile(b'[^%s]+' % re.escape(string.printable.encode('ascii')))
a = []
b = []
t = open('test.txt','w')
with open('tstbd.mrd', "rb") as f:
    buffer = b''
    for chunk in iter(lambda: f.read(2048), b''):
        splitresult = nonprintable.split(buffer + chunk)
        buffer = splitresult.pop()
        for string in splitresult:
            if string:
                t.write((string.decode('ascii')))
    if buffer:
        t.write((buffer.decode('ascii')))
