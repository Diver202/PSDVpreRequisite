def median(array):
    array.sort()
    if len(array)%2==0:
        index = int(len(array)/2)
        return (array[index] + array[index-1])/2
    else:
        index = int((len(array)-1)/2)
        return array[index]

def mean(array):
    return sum(array)/len(array)

array = [3, 5, 7, 9, 11, 13]
array.insert(3,6)
print(array)
array.pop(array.index(7))
print(array)
array = array[::-1]
print(array)
print("mean of modified array:",mean(array))
print("median of modified array:",median(array))
