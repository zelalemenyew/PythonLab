from collections import Counter

def char_frequency(string):
    # create a dictionary to store the frequency count
    freq_count = Counter(string)
    # print the frequency count of each character
    for key, value in freq_count.items():
        print(f'{key}: {value}')

# get input string from user
string = input("Enter a string: ")

# call the function to get the character frequency count
char_frequency(string)
