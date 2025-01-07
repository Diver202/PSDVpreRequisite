import matplotlib.pyplot as plt

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

def mode(array):
    hashmap = {}
    for i in array:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1
    return max(hashmap , key = hashmap.get)


numbers = [54,36,43,56,5,76,8,24,53,46,7,5,8,46,54,7,47,8,32,55,4,36,36]
print("Mean of the numbers is:", mean(numbers))
print("Median of the numbers is:", median(numbers))
print("Mode of the numbers is:", mode(numbers))
print("Standard Deviation of the numbers is:", std(numbers))

plt.boxplot(numbers)
plt.title("Box Plot of Data")
plt.xlabel("Values")
plt.grid(True)
plt.show()