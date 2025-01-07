numbers = [1,2,3,1,42,5,4,6,3,65,7,4,64,37,48,5,5976,2,52,3]
with open("Jupyter notebook/numbers.txt","w") as f:
    for number in numbers:
        f.write(f"{number}\n")
    f.close()

with open("Jupyter notebook/numbers.txt","r") as f:
    sum = 0
    for number in f:
        sum += int(number)
    print("Sum of the numbers is:", sum)
    f.close()
