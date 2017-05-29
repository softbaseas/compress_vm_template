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
    #print "Disk %s = %s" % (count,disk)
    diskpath,diskname = os.path.split(disk)
    filename = "%s%s" % (dstroot,diskname)
    print "Copying %s to %s" % (diskname,dstroot)

    # TODO: copy the vm.cfg file to dstroot and replace diskpath with dstroot in that new vm.cfg file.
    # TODO: Make a script that reads the os simple name from vm.cfg file and make it easier to fetch the right template

    #copyfile(disk,filename)
    #copyfile(disk,diskname)
    #file = open(diskname,"w")
    #file.write(disk)
    #file.close
    count += 1;
