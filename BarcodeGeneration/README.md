# Barcode Generation

Program to generate SVG barcodes for use with bookworm.py.

## How to use

- Edit line 18 of generate.py, and change the last 4 digits of 1000000001000 to the amount of codes to generate. For example, to generate 2305 codes, change it to 1000000002305.

- Install `python-barcode` via pip.

- Run generate.py.

- This will fill the folder with one SVG for each code. Print these and give them to your users.

- This will also fill numbers.csv with one line for each number. Feel free to add names next to each number for easy tracking of users. bookworm.py does not rely on numbers.csv, however.
