def mean(array):
    return sum(array)/len(array)

def std(array):
    avg = mean(array)
    variance = 0
    for value in array:
        variance += (avg - value)**2
    variance = variance/len(array)
    return round(variance**0.5,2)

def median(array):
    array.sort()
    if len(array)%2==0:
        index = int(len(array)/2)
        return (array[index] + array[index-1])/2
    else:
        index = int((len(array)-1)/2)
        return array[index]


array = list(range(1,21))
Sum = 0
product = 1
for i in array:
    if i%2==0:
        Sum+=i
    else:
        product*=i
print("Sum of even numbers is:", Sum)
print("product of odd numbers is:", product)
print("Mean of the list is:", mean(array))
print("Median of the list is:", median(array))
print("Standard deviation of the list is:", std(array))
