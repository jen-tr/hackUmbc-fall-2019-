from pymongo import MongoClient
import random


def hello_world(request):
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }

        return ('', 204, headers)

    client = MongoClient('35.230.173.155', 14532)
    db = client['stox_database']
    stocks = list(db.values.find())
    s = db.values.count()
    s2 = len(stocks)
    request_json = request.get_json(silent=True)
    n = 1
    # return "Request_json" + request_json

    if request_json and 'number' in request_json:
        number = request_json['number']
    else:
        number = '3'

    number = int(number)

    number = random.randint(0, 4)


    headers = {
        'Access-Control-Allow-Origin': '*'
    }
    return str(stocks[number]["symbol"])
# return str(stocks[0]["symbol"]) + " you did it!", 204, headers)
