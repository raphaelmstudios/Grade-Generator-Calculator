#!/bin/bash
# This is a script that archives any CSV files in the current directory and logs it in another file 
echo "********STARTING ARCHIVING PROCESS********"

#Check if the directory archive exists and create if it doesnt
mkdir -p archive

# Find all the CSV files
for file in *.csv; do
       if [ ! -e "$file" ]; then
        echo "No CSV files found."
        exit 0
       	fi

     # Creating the timestamp
    timestamp=$(date +%Y%m%d-%H%M%S)

    # Creating the new filename
    original_name="${file%.csv}"
    modified_filename="${original_name}-${timestamp}.csv"

    echo "Processing: $file"
    echo "New filename: $modified_filename"

    cat >> organizer.log <<EOF
========================================
[$(date '+%Y-%m-%d %H:%M:%S')] Archiving: $file
New filename: $modified_filename
----------------------------------------
File Contents:
$(cat "$file")
========================================

EOF
    # Move file to archive
    mv "$file" "archive/$modified_filename"
    echo "Moved to archive"

    chmod 700 organizer.log
done

echo "********ARCHIVAL PROCESS COMPLETE********"
