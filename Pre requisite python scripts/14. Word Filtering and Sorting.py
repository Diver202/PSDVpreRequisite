import matplotlib.pyplot as plt
def wordHandler(string):
    words = string.split()
    i = 0
    handle = list(word for word in words if len(word)>=4)
    handle.sort()
    dic = {}
    for word in handle:
        if word not in dic:
            dic[word] = len(word)
    plt.bar(dic.keys(),dic.values())
    plt.title("Frequency of different word lengths in the list")
    plt.ylabel("Frequency")
    plt.xlabel("Word length")
    plt.show()
    return handle

print(wordHandler("The quick brown fox jumps over the lazy dog"))

