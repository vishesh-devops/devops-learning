#!/bin/bash
echo "Starting backup..."
mkdir -p backups
cp notes.txt backups/notes_backup_$(date +%Y-%m-%d).txt
echo "Backup complete! File saved in backups folder"
ls backups/

