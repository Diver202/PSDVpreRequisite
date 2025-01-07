import random
import matplotlib.pyplot as plt

def mean(array):
    return sum(array)/len(array)

with open("Jupyter notebook/randomNumbers.txt","w") as f:
    for i in range(100):
        f.write(f"{random.randint(1,50)}\n")
    f.close()
with open("Jupyter notebook/randomNumbers.txt","r") as f:
    s = 0
    array = []
    for number in f:
        array.append(int(number))
    array.sort()
    f.close()


print("Mean of the numbers is:", mean(array))
plt.hist(array, 100)
plt.xlabel("Number")
plt.ylabel("Random Frequency")
plt.title("100 generations of random numbers from 1-50")
plt.show()
