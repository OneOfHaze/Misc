#!/usr/bin/python3

import sys, getopt, os.path
from ODSReader import ODSReader


def main(argv):
    inputFilename = ''
    outputFilename = ''

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
    print('Opened file: ', outputFilename)
    
    # Open input spreadsheet and grab sheet 1
    inputFile = ODSReader(inputFilename, clonespannedcolumns=True)
    sheet1  = inputFile.getSheet(u'Sheet1')
    print ('Opened input file, starting build...')

    # Build output string
    outputFile.write('using UnityEngine;\nusing System.Collections;\nusing System;\n\npublic static class LOC_Strings\n{\n\n\tpublic enum tLOC_Identifier\n\t{\n')

#    for i in range(len(sheet1)):
#       for j in range(len(sheet1[i])):
#            print (sheet1[i][j])

    for i in range (len(sheet1)):
        outputFile.write ( '\t\t_' + sheet1[i][0] + ' = ' + str(i) + ',\n' )

    outputFile.write ('\t};\n\n')

    print('English strings ...')
    outputFile.write('\tpublic static string[] LOC_EnglishStrings = {\n' )

    for i in range (len(sheet1)-1):
        outputFile.write('\t\t\"'+ sheet1[i][1] + '\",\n')

    outputFile.write('\t\"'+ sheet1[len(sheet1)-1][1] + '\"\n\t};\n}')


    outputFile.close()

if __name__ == "__main__":
    main(sys.argv[1:])
