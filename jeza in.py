# Function to count character frequency
def char_frequency(string):
    # Initialize an empty dictionary
    char_count = {}
    # Iterate through each character in the string
    for char in string:
        # If the character is already in the dictionary, increment its count by 1
        if char in char_count:
            char_count[char] += 1
        # If the character is not in the dictionary, add it with a count of 1
        else:
            char_count[char] = 1
    # Return the dictionary with the character frequency count
    return char_count

# Take input from the user
string = input("Enter a string: ")

# Call the function and store the result in a variable
result = char_frequency(string)

# Print the result in the desired format
for key in result:
    print(str(result[key]) + " " + key + "'s,")
    """Name : Jeza Shifa
    Id : 1648
    """
