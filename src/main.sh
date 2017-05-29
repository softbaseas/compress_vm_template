#!bin/bash
# author: Anders Wiberg Olsen (anders@wiberg.tech)

echo "Choose one of the following possibilities:"
echo " 1 - "
echo " q - Exit"

while true; do
  read -p "Choice: " choice
  case $choice in
    [1]*) ;;
    [q]*) exit 0;;
  esac
done
