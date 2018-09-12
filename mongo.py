import urllib3
import json
import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://admin:admin123@ds022408.mlab.com:22408/library')
db = client.library
urllib3.disable_warnings()
http = urllib3.PoolManager()
while True:
    query = input('Scan your barcode: ')
    request = http.request('GET', f'https://api.upcitemdb.com/prod/trial/lookup?upc={query}')
    data = request.data.decode('utf-8')
    jsondata = json.loads(data)
    bookname = jsondata['items'][0]['title']
    print(bookname)
    bookdata = {"title": f"{bookname}",
                "taken": "jeff"}
    books = db.books
    books_id = books.insert_one(bookdata).inserted_id
    print(books_id)
