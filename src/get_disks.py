#!/usr/bin/python
import sys
import shutil

disks = sys.argv[1].replace("\'", "")

dstroot = "./test-folder"

#os.makedirs(dstroot)

count = 0
for disk in disks.split(","):
    print "Disk %s = %s" % (count,disk)
    diskname = "disk%s" % (count)
    file = open(diskname,"w")
    file.write(disk)
    file.close
    count += 1;
