#!/bin/bash
# author: Anders Wiberg Olsen (anders@wiberg.tech)

vmfile=$1

if [ -z ${1+x} ]; then
  echo "Usage: ./compress_template.sh <path to vm.cfg file>"
else
  echo "Argument is set: $vmfile"
fi
