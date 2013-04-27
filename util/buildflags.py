#!/usr/bin/python3

# Super hack-y method of converting CSV values into a JSON string
# corresponding to all of the return values of the SEOmoz API.
#
# Works.

import csv
import sys

HEADERS = ['response','human', 'flag', 'free', 'category']

def main():
    source = sys.argv[1] if len(sys.argv) > 1 else None

    if not source:
        exit('Invalid filename.')

    data = {}

    with open(source, 'r') as f:
        for row in csv.reader(f):
            row_data = {}
            for i in range(1,5):
                row_data[HEADERS[i]] = row[i]
                
            data[row[0]] = row_data

    with open('bitflags.json', 'w') as w:
        w.write(str(data).replace('\'','\"'))

if __name__ == '__main__':
    sys.exit(main())
