from collections import Counter

def char_frequency(string):
    count = Counter(string)
    for key, value in count.items():
        print(key + ": " + str(value))

string = input("Enter a string: ")
char_frequency(string)