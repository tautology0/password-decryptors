#!/usr/bin/env python

import sys
from base64 import b64decode

# The password is stored in %appdata%\Kalypso Media\Launcher\launcher.ini
# under the section [styx user].
# The password is xor'd against a static key and base64'd

# static key
key="lwSDFSG34WE8znDSmvtwGSDF438nvtzVnt4IUv89"

# xorstring(s, k)
# xors the two strings
def xorstring(s, k):
   return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(s,k))

# Pass the encoded password as $ARG1
b64pw = sys.argv[1]

if not b64pw:
   print "No password passed"
   print "Syntax: " + sys.argv[0] + " <encoded password>"
   sys.exit(1)

cookedpw=b64decode(b64pw)
rawpw=xorstring(cookedpw, key)
print rawpw

   

