#!/usr/bin/python3

import sys, getopt, os.path
from ODSReader import ODSReader

def main(argv):
    inputfile = ''
    outputfile = ''

    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ('File error: test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFilename = arg
        elif opt in ("-o", "--ofile"):
            outputFilename = arg


    if os.path.isfile(inputFilename):
        print('Found file:', inputFilename)
    else:
        print('Unable to find file:', inputFilename)
        sys.exit()


    # Open our output file...
    outputFile = open(outputFilename, 'w')
    
    inputFile = ODSReader(inputFilename, clonespannedcolumns=True)
    sheet1  = inputFile.getSheet(u'Sheet1')


    for i in range(len(sheet1)):
        for j in range(len(sheet1[i])):
            print (sheet1[i][j])


if __name__ == "__main__":
    main(sys.argv[1:])
