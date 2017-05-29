#!/usr/bin/python
import sys
from shutil import copyfile
import os

disks = sys.argv[1].replace("\'", "")
dstroot = "./"

if (len(sys.argv) == 2):
    dstroot = "./test-folder/"
else:
    dstroot = sys.argv[2]

if not os.path.exists(dstroot):
    os.makedirs(dstroot)

count = 0
for disk in disks.split(","):
    print "Disk %s = %s" % (count,disk)
    diskname = "%sdisk%s" % (dstroot,count)
    print os.path.basename(disk)
    #copyfile(disk,diskname)
    #file = open(diskname,"w")
    #file.write(disk)
    #file.close
    count += 1;
