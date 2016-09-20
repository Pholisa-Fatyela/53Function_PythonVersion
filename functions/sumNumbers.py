def sum_numbers(number):
    theSum = 0
    myList = []
    for i in range(1,number+1):
		myList.append(i)
    for result in myList:
        theSum = theSum + result
    return theSum
