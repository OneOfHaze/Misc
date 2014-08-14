#!/bin/bash
# Set the field seperator to a newline
$ext='flac'

while read line ;do
   echo "Found File:"
   echo $line

   output=$(echo $line | sed 's/\(.*\)\..*/\1/')

   if [ -f "$output.flac" ]
       then
       echo "File already exists"
       else
       echo "Converting to: "
       echo $output".flac"
       avconv -i "$line" -acodec flac "$output.flac"
   fi
done < ./FilesToConvert.txt