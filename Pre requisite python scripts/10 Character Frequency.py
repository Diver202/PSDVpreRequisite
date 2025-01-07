import matplotlib.pyplot as plt
def characterFrequency(string):
    string = string.lower()
    characters = {}
    for char in string:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    return characters

characters = characterFrequency(input("Enter the string:"))
plt.bar(characters.keys(),characters.values())
plt.title = "Frequency distribution of characters in the given string"
plt.xlabel = "Characters"
plt.ylabel = "Frequency"
plt.show()
