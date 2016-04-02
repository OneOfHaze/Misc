#!/bin/bash

virtualenv -p /usr/bin/python3 py3env
source py3env/bin/activate
python3 generate_loc.py -i ./GameStrings.ods -o LOC_Strings.cs

