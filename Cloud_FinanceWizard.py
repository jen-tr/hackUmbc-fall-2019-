from pymongo import MongoClient

def financeWizard(request):
    #get the json data
    request_json = request.get_json()
	#get budget
    if request_json and 'message' in request_json:
	    budget = float(request_json['message'])
    else:
        budget = 0

    #connect to database
    client=MongoClient("35.230.173.155",14532)
    db=client['stox_database']

    #pull values from database
    stocks = list(db.values.find())

    #find max
    maxVal = None
    for stockDict in stocks:
        if (float(stockDict["val"]) <= budget) and ((maxVal is None) or (maxVal < float(stockDict["val"]))):
            maxVal = stockDict["val"]
            maxSymbol = stockDict["symbol"]

    if maxVal == None:
        return "You can't afford any stocks."
    else:
        return ("With your budget, you can purchase stock: " + str(maxSymbol) + " at the price of $" + str(maxVal))
