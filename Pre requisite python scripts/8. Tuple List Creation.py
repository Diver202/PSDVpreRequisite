import matplotlib.pyplot as plt
points = []
for i in range(1,11):
    points.append((i,i**2))
x = [i[0] for i in points]
y = [i[1] for i in points]
plt.scatter(x,y,c = "red")
plt.show()