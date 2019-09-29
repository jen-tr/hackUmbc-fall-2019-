from pymongo import MongoClient


if __name__ == "__main__":

    #prompt for budget
    budget = float(input("what is your budget? "))

    #connect to database
    print("[~] Connecting to DB")
    client=MongoClient("172.17.0.2",27017) #After spinning up the docker container,$
    db=client['stox_database'] #gimme a databasse to query against
    print("[*] Connection OK!")

    #pull values from database	
    stocks = list(db.vals.find())
    print("[*] Pulled Live Stock Values!")

    #find max
    maxVal = None
    for stockDict in stocks:
        print("stockDict: " + stockDict.__repr__())
        if (float(stockDict["val"]) <= budget) and ((maxVal is None) or (maxVal < float(stockDict["val"]))):
            maxVal = stockDict["val"]
            maxSymbol = stockDict["symbol"]

    if maxVal == None:
        print("You can't afford any stocks.")
    else:
        print("With your budget, you can purchase stock: " + maxSymbol + " at the price of $" + str(maxVal))

