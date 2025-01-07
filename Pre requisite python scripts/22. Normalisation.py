import matplotlib.pyplot as plt
def normalise(array):
    handle = []
    minimum = min(array)
    maximum = max(array)
    for i in array:
        n = (i - minimum)/(maximum - minimum)
        handle.append(n)
    return handle

array = [12,13,35,3,67,86,34,56,90,99,12,100,7,23,54]
normalised = normalise(array)
print(normalised)
plt.plot(normalised, marker='o', linestyle='-', color='blue', label='Normalized Data')
plt.title("Normalized Data Line Plot")
plt.xlabel("Index")
plt.ylabel("Normalized Value")
plt.grid(True)
plt.legend()
plt.show()