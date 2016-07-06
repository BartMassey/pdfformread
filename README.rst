pdfformread
--------------------------

Copyright (c) 2016 Bart Massey

This Python 2 library and command-line app facilitate
getting form data from PDF forms, using the PDFMiner
(http://www.unixuser.org/~euske/python/pdfminer) library for
extraction.  The code is originally from
http://stackoverflow.com/q/3984003/364875 but with minor
changes for 2016 and for app.

There are a lot of things that need to be improved here:

* Unicode and other character encoding handling is kludgy at best.

* Only text and selection elements of forms are supported.

* Subforms aren't supported.

This code is available under the "MIT License".
Please see the file COPYING in this distribution
for license terms.
