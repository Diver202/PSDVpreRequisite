import matplotlib.pyplot as plt
lOs = ["lmao","Divyansh","hfaui","blith","supercalifragilistic","a"]
def vowelWordCount(array):
    count = 0
    for word in array:
        if word.lower()[0] in 'aeiou':
            count+=1
    return count

longest = max(lOs , key = len )
dic = {}
for word in lOs:
    if len(word) not in dic:
        dic[len(word)] = 1
    else:
        dic[len(word)] += 1

print("longest string is", longest)
print("Number of strings starting with a vowel are", vowelWordCount(lOs))
plt.bar(dic.keys(),dic.values())
plt.title("Frequency of different string lengths in the list")
plt.ylabel("Frequency")
plt.xlabel("String length")
plt.show()
