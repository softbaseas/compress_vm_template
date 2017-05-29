#!/bin/bash
# author: Anders Wiberg Olsen (anders@wiberg.tech)

if [ -z ${1+x} ]; then
  echo "No argument is set..."
else
  echo "Argument is set: $1"
fi
