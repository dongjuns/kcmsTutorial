#!/usr/bin/env python

import os, sys

if ( len( sys.argv) != 2 ) :
    print "wrong argument."

sum =0
for x in range(10*(int(sys.argv[1])+1))[-10:] :
    print x
    sum = sum+x

ofile = open("out.txt","w")
ofile.write("Sum is %d\n"%(sum))
ofile.close()
