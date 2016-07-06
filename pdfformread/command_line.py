#!/usr/bin/python2
# Copyright (c) 2016 Bart Massey
# This code is available under the "MIT License".
# Please see the file COPYING in this distribution
# for license terms.

# Command line PDF form data extractor.

# Originally from
#   http://stackoverflow.com/q/3984003/364875
# but with minor changes for 2016 and for app.

from argparse import ArgumentParser
import json
import pickle
import pprint
from sys import stdout, stderr

import pdfformread

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
    parser.add_argument('-r', '--raw', action='store_true', default=False,
                      help='Format output un-prettyprinted')
    return parser.parse_args()

def main():
    args = parse_cli()
    form = pdfformread.load_form(args.file)
    if not form:
        stderr.write(args.file + ": no form\n")
        exit(1)
    if args.out:
        outfile = open(args.out, 'w')
        assert outfile
    else:
        outfile = stdout
    assert not args.json or not args.pickle
    try:
        if args.json:
            if args.raw:
                indent = None
            else:
                indent = 2
            json.dump(form, outfile, indent=indent)
        elif args.pickle:
            pickle.dump(form, outfile)
        else:
            if args.raw:
                form_string = str(form)
            else:
                pp = pprint.PrettyPrinter(indent=2)
                form_string = pp.pformat(form)
            outfile.write(form_string)
    except Exception, e:
        stderr.write(args.file + ": dump failed: " + str(e) + "\n")
        exit(1)
