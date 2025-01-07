def anagramFinder(word, words):

    sortedWord = sorted(word)
    return [w for w in words if sorted(w) == sortedWord]

print(anagramFinder("listen", ["enlist", "google", "inlets", "banana"]))