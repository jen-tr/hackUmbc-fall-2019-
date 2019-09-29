#!/usr/bin/python3
from yahoo_fin import stock_info as si
from pymongo import MongoClient
splash = '''
 ____  _             _      ____        _        -\r\n/ ___|| |_ ___   ___| | __ |  _ \\  __ _| |_ __ _| |__   __ _ ___  ___ \r\n\\___ \\| __/ _ \\ / __| |/ / | | | |/ _` | __/ _` | '_ \\ / _` / __|/ _ \\\r\n ___) | || (_) | (__|   <  | |_| | (_| | || (_| | |_) | (_| \\__ \\  __/\r\n|____/ \\__\\___/ \\___|_|\\_\\ |____/ \\__,_|\\__\\__,_|_.__/ \\__,_|___/\\___|\r\n\r\n _   _           _       _            \r\n| | | |_ __   __| | __ _| |_ ___ _ __ \r\n| | | | '_ \\ / _` |/ _` | __/ _ \\ '__|\r\n| |_| | |_) | (_| | (_| | ||  __/ |   \r\n \\___/| .__/ \\__,_|\\__,_|\\__\\___|_|   \r\n
'''

print(splash)
print("\n=========================\nWith love from Zaine\n=========================\n")

print("[~] Connecting to DB")
client=MongoClient("172.17.0.2",27017) #After spinning up the docker container, cat /etc/hosts to find it's IP. fill that shit in here
db=client['stox_database'] #gimme a databasse to query against
print("[*] Connection OK!")

stox = {'aapl','nvda','x','amzn','amd','ibm'} #add some more symbols here for fun and profit
print("[~] Starting Iteration")

while True:
	for i in stox:
		try:
			vals=db.values #use the values collection in the db
			val=si.get_live_price(i) #query Yahoo for the price
			postme = {} # create a dictionary to throw to the database
			postme["symbol"]=i # fill in the symbol key
			postme["val"]=val # fill in the value key
			try: #this block will execute if the value is in the database
				p=vals.find({"symbol":i})[0] # gimme a cursor for symbol, and get the first value in the cursor
				db.vals.update_one({'_id': p['_id']},{"$set":postme}, upsert=False) #if we pass the above line, the value is in the DB. Update it's value.
			except Exception as e: # this block will execute  if the value is not in the database
				print("[~] Adding new symbol to DB: "+i)
				result = vals.insert_one(postme) # add a value to the DB if it's not present
			print("[*] Post OK for "+i)
		except Exception as e:
			print("[E] Error on "+i+". Symbol may not exist")
			print("\t"+str(e))
