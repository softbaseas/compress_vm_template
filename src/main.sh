#!/bin/bash
# author: Anders Wiberg Olsen (anders@wiberg.tech)

vmfile=$1

if [ -z ${1+x} ]; then
  echo "Usage: ./compress_template.sh <path to vm.cfg file>"
else
  echo "Argument is set: $vmfile"
  ./src/get_disks.py `grep disk $vmfile | sed 's/disk = \[//g' | sed 's/file://g' | sed 's/xv\w\+//g' | sed 's/,,w!//g' | sed 's/,,w//g' | sed 's/ //g' | sed 's/.$//'`
fi



# grep disk test_vm.cfg : Get the line with all disks
# sed 's/disk = \[//g'  : Remove "disk = [" from the string
# sed 's/file://g'      : Remove "file:" from the string
# sed 's/xv\w\+//g'     : Remove all words starting with "xv"
# sed 's/,,w!//g'       : Remove ",,w!" from the string
# sed 's/,,w//g'        : Remove ",,w" from the string
# sed 's/ //g'          : Remove all spaces in the string
# sed 's/.$//'          : Remove the last character in the string ("]")

#disks_str=`grep disk $vmfile | sed 's/disk = \[//g' | sed 's/file://g' | sed 's/xv\w\+//g' | sed 's/,,w!//g' | sed 's/,,w//g' | sed 's/ //g' | sed 's/.$//'`
#disks=$(echo $disks_str | tr "," "\n")

#for disk in $disks do
#  echo "> $disk"
#done
