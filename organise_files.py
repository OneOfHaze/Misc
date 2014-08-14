#!/usr/bin/python3

from pathlib import Path
import os
import shutil

def recursePath(p ):
	for item in p.iterdir():
		if item.is_dir():
			checkDirectory(item)
			recursePath(item)

def checkDirectory(dir):
	m4a = list(dir.glob('*.m4a'))
	flac = list(dir.glob('*.flac'))
	mp3 = list(dir.glob('*.mp3'))

	if ( len(mp3) > 0 and len(m4a) > 0 and len(flac) == 0 ):
		print("\t", dir.resolve(), " -- 2 folders -- (mp3 and m4a mixed)")
		moveFiles( mp3, makeDir("mp3", dir) )
		moveFiles( m4a, makeDir("m4a", dir) )

	elif ( len(mp3) > 0 and len(m4a) == 0 and len(flac) > 0 ):
		print ("\t", dir.resolve(), " -- 2 folders -- (mp3 and flac mixed)")
		moveFiles( mp3, makeDir("mp3", dir) )
		moveFiles( flac, makeDir("flac", dir) )

	elif (len(mp3) == 0 and len(m4a) > 0 and len(flac) > 0 ):
		print ("\t", dir.resolve(), " -- 2 folders -- (flac and m4a mixed)")
		moveFiles( m4a, makeDir("m4a", dir) )
		moveFiles( flac,	makeDir("flac", dir) )

	elif (len(mp3) > 0 and len(m4a) > 0 and len(flac) > 0 ):
		print ("\t", dir.resolve(), " -- 3 folders -- (mp3, flac and m4a mixed)" )
		moveFiles( mp3, makeDir("mp3", dir) )
		moveFiles( m4a, makeDir("m4a", dir) )
		moveFiles( flac, makeDir("flac", dir) )


def makeDir(type, dir):
	try:
		pathString = dir.as_posix() + "/" + type
		os.mkdir( pathString ) 
		return pathString
	except OSError:
		print ("Failure to create mp3 folder in: ", dir.resolve())
		quit()

def moveFiles(files, path):
	for file in files:
		try:
			shutil.move(file.as_posix(), path)
		except OSError:
			print("Unable to move to move " + file.as_posix() + " to folder: " + path )

rootPath = Path('.')
recursePath(rootPath)
