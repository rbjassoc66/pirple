def addToList(parm):
    if parm in myUniqueList:
        myLeftovers.append(item)
        print True
        return True
    else:
        myUniqueList.append(parm)
        print(False)
        return False


myUniqueList = []
myLeftovers =[]

item = raw_input('Try to add an item to the list, if you want to stop type "stop" ')

while item != 'stop':
    addToList(item)
    item = raw_input('Try to add an item to the list, if you want to stop type "stop" ')



print('Here is my unique list of items ',myUniqueList)

print('Here is my list of left over items ',myLeftovers)








