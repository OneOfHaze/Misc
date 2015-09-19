#!/usr/bin/python3

import sys, getopt, os.path

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
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

#           print ('Input file is ', inputfile)
#           print ('Output file is ', outputfile)

    if os.path.isfile(inputfile):
        print('Found file:', inputfile)
    else:
        print('Unable to find file:', inputfile)
        sys.exit()



if __name__ == "__main__":
    main(sys.argv[1:])
