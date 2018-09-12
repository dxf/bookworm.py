import barcode
import sys
import csv
barcode.PROVIDED_BARCODES
[u'code39', u'code128', u'ean', u'ean13', u'ean8', u'gs1', u'gtin',
 u'isbn', u'isbn10', u'isbn13', u'issn', u'jan', u'pzn', u'upc', u'upca']
EAN = barcode.get_barcode_class('ean13')
code = 1000000000000
sheet = "numbers.csv"
codes = []

while True:
    convert = str(code)
    ean = EAN(convert)
    fullname = ean.save(code)
    codes.append(str(code))
    code += 1
    if code > 1000000001000:
        with open(sheet, 'w',  newline='\n') as jeff:
            writer = csv.writer(jeff)
            for numbers in codes:
                writer.writerow([numbers])
        sys.exit()
while True:
    convert = str(code)
    ean = EAN(convert)
    fullname = ean.save(code)
    with open(sheet, 'w') as jeff:
        writer = csv.writer(jeff)
        writer.writerows(convert)
    code += 1
    if code == 1000000000009:
        jeff.close()
        sys.exit()
