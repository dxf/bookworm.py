import urllib3
import json
import csv
import time

urllib3.disable_warnings()
http = urllib3.PoolManager()
clear = "\n" * 1000
while True:
    card = input('Welcome! To exit at any time, scan the exit code with the barcode scanner, located below the screen. \nScan your card: ')
    print(clear)
    print(f'Logged in as {card}.\n')
    
    service = input('What would you like to do? (Scan the code below the screen!) ')
    if service == "9999999999994":
        print(clear)
        query = input('You selected Check Out. Awesome! Let\'s check out your book. Scan the barcode of your book (usually on the back): ')
        request = http.request('GET', f'https://api.upcitemdb.com/prod/trial/lookup?upc={query}')
        data = request.data.decode('utf-8')
        jsondata = json.loads(data)
        try:
            bookname = jsondata['items'][0]['title']
            with open('books.csv', 'w') as spreadsheet:
                reader = csv.reader(spreadsheet)
                fieldnames = [f'title','taken']
                bookdata = {"title": f"{bookname}",
                            "taken": f"{card}"}
                try:
                    writer = csv.DictWriter(spreadsheet, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerow(bookdata)
                    spreadsheet.close()
                    print(f'Successfully checked out {bookname}! Thanks for using the library. Restarting in 5 seconds.')
                    time.sleep(5)
                    print(clear)
                except(PermissionError):
                    print('Failed to write to spreadsheet. Ask the librarian to try and solve the issue and/or check out manually.')
        except(IndexError):
            print('Book not recognised. Did you scan the right barcode? The long one, usually on the back of the book. Otherwise, check out manually with the librarian.')
    if service == "9999999999993":
        print(clear)
        query = input('You selected Return. Awesome! Let\'s return your book. Scan the barcode of your book (usually on the back): ')
        print(clear)
        request = http.request('GET', f'https://api.upcitemdb.com/prod/trial/lookup?upc={query}')
        data = request.data.decode('utf-8')
        jsondata = json.loads(data)
        try:
            bookname = jsondata['items'][0]['title']
            with open('books.csv', 'w') as spreadsheet:
                reader = csv.reader(spreadsheet)
                fieldnames = [f'title','taken']
                bookdata = {"title": f"{bookname}",
                            "taken": "returned"}
                try:
                    writer = csv.DictWriter(spreadsheet, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerow(bookdata)
                    spreadsheet.close()
                    print(f'Successfully returned {bookname}! Thanks for using the library. Restarting in 5 seconds.')
                    time.sleep(5)
                    print(clear)
                except(PermissionError):
                    print('Failed to write to spreadsheet. Ask the librarian to try and solve the issue and/or check in manually.')
                    time.sleep(5)
                    print(clear)
        except(IndexError):
            print('Book not recognised. Did you scan the right barcode? The long one, usually on the back of the book. Otherwise, check out manually with the librarian.')
            time.sleep(5)
            print(clear)
     if service == "9999999999992":
        print('Exiting. Thanks for using the library!')
    else:
        print('Function not recognised! Try scanning the function code again, or ask the librarian to check you out manually.')
        time.sleep(5)
        print(clear)
