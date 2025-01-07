def removeDuplicates(array):
    handler = []
    for element in array:
        if element in handler:
            continue
        else:
            handler.append(element)
    return handler

def mean(array):
    return sum(array)/len(array)

def median(array):
    array.sort()
    if len(array)%2==0:
        index = int(len(array)/2)
        return (array[index] + array[index-1])/2
    else:
        index = int((len(array)-1)/2)
        return array[index]

array = [1,2,3,2,42,4,645,7,4,532,46,3,563,57,73,6,436,534,5,1,23,41,352,4,78]
array = removeDuplicates(array)
print("The list after removing duplicate elements is:", array)
print("Mean of the new list after removing duplicates is:", mean(array))
print("Median of the new list after removing duplicates is:", median(array))


