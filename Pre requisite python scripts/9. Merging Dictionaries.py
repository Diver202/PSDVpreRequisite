dict1 = {'a': 10, 'b': 20}
dict2 = {'b': 5, 'c': 15}
handleDict = dict1
for key in dict2:
    if key in handleDict:
        handleDict[key]+=dict2[key]
    else:
        handleDict[key]=dict2[key]
print(handleDict)