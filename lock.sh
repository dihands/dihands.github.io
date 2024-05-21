#!/bin/bash
# This script locks a file with a password using the zip command

# Check that a file has been provided as an argument
if [ $# -eq 0 ]; then
  echo "Usage: $0 <file>"
  exit 1
fi

# Check that the file exists
if [ ! -f "$1" ]; then
  echo "File not found: $1"
  exit 1
fi

# Prompt the user for a password
echo -n "Enter password to lock file: "
read -s password

# Lock the file with the given password
zip -e -P "$password" "$1.zip" "$1"

# Remove the original file
rm "$1"

echo "File locked with password: $1.zip"
