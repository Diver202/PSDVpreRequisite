string = input()
newstring = ""
for i in string:
    if not(i.isspace()):
        newstring+=i.lower()
print(newstring == newstring[::-1])

    