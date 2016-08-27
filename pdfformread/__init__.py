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

class FormParseException(Exception):
    pass

def load_form(filename):
    """Load pdf form contents into a dictionary"""
    with open(filename, 'rb') as file:
        try:
            parser = PDFParser(file)
            doc = PDFDocument(parser)
            parser.set_document(doc)
            if not 'AcroForm' in doc.catalog:
                return None
            fields = resolve1(doc.catalog['AcroForm'])
            if fields == None or 'Fields' not in fields:
                return None
            fieldlist = []
            for f in fields['Fields']:
                field = resolve1(f)
                if field == None:
                    return None
                fieldlist.append(load_field(field))
            fieldset = dict()
            for f in fieldlist:
                if f == None:
                    continue
                k, v = f
                fieldset[k] = v
            return fieldset
        except UnicodeDecodeError, e:
            raise FormParseException(filename + ": unicode error: " + str(e))

def load_field(field):
    """load form field"""
    def uniflail(stringish):
        def uni8(stringish):
            try:
                return unicode(stringish, encoding='utf8')
            except UnicodeDecodeError:
                return unicode(stringish, encoding='iso-8859-1')
        if stringish == None:
            return None
        if len(stringish) < 2:
            return uni8(stringish)
        b0 = ord(stringish[0])
        b1 = ord(stringish[1])
        if (b0 == 0xff and b1 == 0xfe) or (b0 == 0xfe and b1 == 0xff):
            return unicode(stringish, encoding='utf16')
        return uni8(stringish)
    typ = field.get('FT').name
    if typ:
        t = field.get('T')
        if not t:
            return None
    if typ == "Tx":
        val = resolve1(field.get('V'))
        if val == None:
            return None
        return (t, uniflail(val))
    elif typ == "Btn":
        val = resolve1(field.get('V'))
        if val == None:
            return None
        return (t, uniflail(val.name))
    else:
        raise FormParseException("unknown field type " + typ)
