array = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 22}, {'name':'Chris', 'age':29}]
def sortDictsByKey(array , key):
    return sorted(array, key = lambda x:x[key])

print(sortDictsByKey(array, 'age'))
