#Program to check if the string is a valid keyword or not

import keyword
keys = ["for", "while", "tanisha", "Ripan", "else", "assert", "shubham"]

for i in range(len(keys)):
    if keyword.iskeyword(keys[i]):
        print(keys[i] + " is a keyword")
    else:
        print(keys[i] + " is not a keyword")
