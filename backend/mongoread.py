def hello_world(request):
    client = MongoClient('35.230.173.155', 14532)
    db = client['stox_database']
    stocks = list(db.vals.find())
    return "apple"
