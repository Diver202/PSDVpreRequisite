import string
import matplotlib.pyplot as plt
with open("Jupyter notebook/beeMovie.txt","r") as f:
    wordMap = {}
    for line in f:
        for punctuation in string.punctuation:
            line = line.replace(punctuation,'')
        words = line.strip().split()
        for word in words:
            if word.lower() not in wordMap:
                wordMap[word.lower()] = 1
            else:
                wordMap[word.lower()] += 1
    f.close()
wordMap = dict(sorted(wordMap.items(), key = lambda item : item[1], reverse = True))
plt.bar(list(wordMap.keys())[:10],list(wordMap.values())[:10])
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Frequency of top 10 words in the Bee Movie")
plt.show()


        