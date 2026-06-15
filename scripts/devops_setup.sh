#!/bin/bash

# Variables
name="Vishesh"
date=$(date +%Y-%m-%d)
log_file="logs/setup_$date.log"

echo "Starting DevOps setup for $name on $date"
echo "Starting DevOps setup for $name on $date" >> $log_file

for folder in scripts logs backups configs
do
if [ -d "$folder" ]
then
echo "Folder $folder already exists"
else
mkdir -p $folder
echo "Created folder $folder"
fi
done
# Backup notes
cp notes.txt backups/notes_backup_$date.txt
echo "Notes backed up successfully"
echo "Notes backed up successfully" >> $log_file
echo "Setup complete!"
echo "Setup complete!">> $log_file

