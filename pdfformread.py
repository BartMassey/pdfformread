#!/usr/bin/python2
# Copyright (c) 2016 Bart Massey
# This code is available under the "MIT License".
# Please see the file COPYING in this distribution
# for license terms.

# Command line PDF form data extractor.

# Originally from
#   http://stackoverflow.com/q/3984003/364875
# but with minor changes for 2016 and for app.

from sys import stdout
from argparse import ArgumentParser
import json
import pickle
import pprint

import pdfformparse

def parse_cli():
    """Load command line arguments"""
    parser = ArgumentParser(description='Dump the form contents of a PDF.')
    parser.add_argument('file', metavar='pdf_form',
                    help='PDF Form to dump the contents of')
    parser.add_argument('-o', '--out', help='Write output to file',
                      default=None, metavar='FILE')
    parser.add_argument('-p', '--pickle', action='store_true', default=False,
                      help='Format output for python consumption')
    parser.add_argument('-j', '--json', action='store_true', default=False,
                      help='Format output as JSON')
    return parser.parse_args()

def main():
    args = parse_cli()
    form = pdfformparse.load_form(args.file)
    if args.out:
        outfile = open(args.out, 'w')
        assert outfile
    else:
        outfile = stdout
    assert not args.json or not args.pickle
    if args.json:
        json.dump(form, outfile)
    elif args.pickle:
        pickle.dump(form, outfile)
    else:
        pp = pprint.PrettyPrinter(indent=2)
        outfile.write(pp.pformat(form))

if __name__ == '__main__':
    main()
