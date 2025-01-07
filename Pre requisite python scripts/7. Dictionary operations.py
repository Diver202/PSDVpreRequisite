import matplotlib.pyplot as plt

def mean(array):
    return sum(array)/len(array)


Marks = {"A":87,
         "B":93,
         "C":12,
         "D":34,
         "E":24,
         "F":65,
         "G":37,
         "H":62,
         "I":20,
         "J":100}

meanMarks = mean(Marks.values())
for name in Marks:
    if Marks[name]> meanMarks:
        print(name)

plt.bar(Marks.keys(),Marks.values())
plt.title = "Marks"
plt.xlabel = "Name"
plt.ylabel = "Marks"
plt.show()
