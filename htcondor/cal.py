#!/usr/bin/env python

import os, sys

if ( len( sys.argv) != 2 ) :
    print "wrong argument."

for x in range(10*(int(sys.argv[1])+1))[-10:] :
    print x
