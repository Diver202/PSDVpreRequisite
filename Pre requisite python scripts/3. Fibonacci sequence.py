#limit N = 1476
import matplotlib.pyplot as plt

def fibonacciList(n):
    array = []
    pen = 1
    ult = 1
    for i in range(n):
        if i==0:
            array.append(pen)
            continue
        array.append(ult)
        pen,ult = ult,pen+ult
    return array

N = int(input())
yAxis = fibonacciList(N)
xAxis = list(range(1,N+1))

plt.plot(xAxis,yAxis)
plt.xlabel("Index")
plt.ylabel("Fibonacci number")
plt.title("Fibonacci number v index")
plt.show()