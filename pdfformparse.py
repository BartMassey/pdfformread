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
        if not 'AcroForm' in doc.catalog:
            return None
        fieldlist = [load_field(resolve1(f)) for f in
                     resolve1(doc.catalog['AcroForm'])['Fields']]
        fieldset = dict()
        for k, v in fieldlist:
            fieldset[k] = v
        return fieldset

def load_field(field):
    """load form field"""
    def uniflail(stringish):
        if stringish == None:
            return None
        if len(stringish) < 2:
            return unicode(stringish, encoding='utf8')
        b0 = ord(stringish[0])
        b1 = ord(stringish[1])
        if (b0 == 0xff and b1 == 0xfe) or (b0 == 0xfe and b1 == 0xff):
            return unicode(stringish, encoding='utf16')
        return unicode(stringish, encoding='utf8')
    typ = field.get('FT').name
    if typ == "Tx":
        return (field.get('T'), resolve1(field.get('V')))
    elif typ == "Btn":
        return (field.get('T'), resolve1(field.get('V')).name)
    else:
        raise FieldTypeException("unknown field type " + typ)
