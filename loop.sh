#!/bin/bash
for folder in scripts logs backups configs
do
 mkdir -p $folder
 echo "Created folder: $folder"
done
echo "All folders created"

