#!/usr/bin/python3

# argTest.py

import argparse

parser= argparse.ArgumentParser()
parser.add_argument("secs", help="convert seconds into more human readable form", type=int)
args= parser.parse_args()

days= args.secs//86400
rem_secs= args.secs%86400

hrs= rem_secs//3600
rem_secs = rem_secs%3600

mins = rem_secs//60

print('Next stake:',days,'days,',hrs,'hours,',mins,'minutes')
  

