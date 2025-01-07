import matplotlib.pyplot as plt
def mean(array):
    return(sum(array)/len(array))

input_numbers = input("Enter a comma-separated list of numbers: ")
numbers = [float(num.strip()) for num in input_numbers.split(",")]

if not numbers:
    raise ValueError("No numbers provided.")

mean_value = mean(numbers)
smallest = min(numbers)
largest = max(numbers)

print(f"Mean: {mean_value}")
print(f"Smallest number: {smallest}")
print(f"Largest number: {largest}")

plt.hist(numbers, bins=10, color='green', edgecolor='black')
plt.title("Histogram of Input Numbers")
plt.xlabel("Number")
plt.ylabel("Frequency")
plt.grid(axis='y', alpha=0.5)


plt.show()

