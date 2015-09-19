Misc
====

Random scripts:

convert_files.sh - Takes filtered directory listing and pushes files through
avconv for conversion to flac. Used it to process 16k m4a files on my NAS


organise_files.py - Recursively walks through a directory structure looking for
folders that contain music files of different types (mp3, m4a, flac). Will
create a new folder for each file type and move all files of that type to the
new folder. Handy for tidying up the 16k flac files you might have created
automatically with convert_files.sh :D

generate_loc - Read a Libre Office Calc spreadsheet and generate a C# file 
containing a set of strings for Localisation. Spreadsheet is ordered by 
column: UID, Lang1, Lang2, ... GameObjects can then set text labels by using
this as a LUT.

