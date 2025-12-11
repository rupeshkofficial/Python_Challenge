"""
Write a function that accepts a string and prints the frequency of each character in the string.

hello
{"h": 1, "e": 1, "l":2, "o": 1}
h occurs 1 times
e occurs 1 times
l occurs 2 times
o occurs 1 times

"""

def charCount(string):
    #my_dict = {} # 1st way to create Blank dictionary
    my_dict = dict() # 2nd way to create Blank dictionary

    for ch in string:
        if ch not in my_dict:
            my_dict[ch] = 1
        else:
            my_dict[ch] += 1
    #print(my_dict)
    for k,v in my_dict.items():
        print(f"{k} occurs {v} times")


charCount("dwgbefreger")