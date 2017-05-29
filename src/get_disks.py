#!/usr/bin/python
import sys
import shutil
import os

disks = sys.argv[1].replace("\'", "")
print "argument length: %s" % (len(sys.argv))

if (len(sys.argv)==2):
    dstroot = "./test-folder"
else:
    dstroot = sys.argv[2]

#os.makedirs(dstroot)

count = 0
for disk in disks.split(","):
    print "Disk %s = %s" % (count,disk)
    diskname = "disk%s" % (count)
    file = open(diskname,"w")
    file.write(disk)
    file.close
    count += 1;
