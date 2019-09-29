



import sys



if __name__ == "__main__":

    budget = raw_input("What is your budget?")

    fobject = file("data.txt","rw")
    stocks = []
    maxVal = None
    maxIndex = 0

    for count,line in enumerate(fobject.readlines()):
        currline = line.split()
        stocks.append({"name":currline[0],"price":currline[1]})

        if float(currline[1]) <= float(budget) and (maxVal is None):
            maxVal = currline[1]
            maxIndex = count

        elif float(currline[1]) <= float(budget) and (float(currline[1]) < maxVal):
            maxVal = currline[1]
            maxIndex = count

    if maxVal == None:
        print("You can't afford any stocks.")

    else:
        print("With your budget, you can purchase stock: " + stocks[maxIndex]["name"] + " at the price of $" + stocks[maxIndex]["price"])

