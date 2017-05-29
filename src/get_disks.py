#!/usr/bin/python
import sys

disks = sys.argv[1].replace("\'", "")

count = 0
for disk in disks.split(","):
    print "Disk %s = %s" % (count,disk)
    count += 1;
