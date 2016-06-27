#!/usr/bin/python2
# Copyright (c) 2016 Bart Massey
# This code is available under the "MIT License".
# Please see the file COPYING in this distribution
# for license terms.

# PDF form data extraction library using pdfminer.

# Originally from
#   http://stackoverflow.com/q/3984003/364875
# but with minor changes for 2016 and for app.

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdftypes import resolve1, PDFObjRef

class FieldTypeException(Exception):
    pass

def load_form(filename):
    """Load pdf form contents into a dictionary"""
    with open(filename, 'rb') as file:
        parser = PDFParser(file)
        doc = PDFDocument(parser)
        parser.set_document(doc)
        fieldlist = [load_fields(resolve1(f)) for f in
                     resolve1(doc.catalog['AcroForm'])['Fields']]
        fieldset = dict()
        for k, v in fieldlist:
            fieldset[k] = v
        return fieldset

def load_fields(field):
    """load form fields"""
    typ = field.get('FT').name
    if typ == "Tx":
        return (field.get('T'), resolve1(field.get('V')))
    elif typ == "Btn":
        return (field.get('T'), resolve1(field.get('V')).name)
    else:
        raise FieldTypeException(typ)
