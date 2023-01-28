import string

    #A FUNCTION USED TO REMOVE PUNCTUATION MARKS
def punctuationRemover(textFile):
    textFile = textFile.translate(textFile.maketrans("", "", string.punctuation))
    return textFile
def wordFinder(textFile):
    wordFound = {}
    for word in textFile.split():
        if word in wordFound:
           wordFound[word] += 1
        else:
           wordFound[word] = 1
    for key in list(wordFound.keys()):
        print(key, end=",")

    # A FUNCTION USED TO COUNT WORD FREQUENCY
def frequency_of_words(textFile):
    word_counts = {}
    for word in textFile.split():
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_words:
        print(f"{word}: {count}")

    # A FUNCTION USED TO COUNT FREQUENCY OF CHARACTERS
def frequency_of_characters(textFile):
    char_counts = {}
    for char in textFile:
        if char==" ":
            continue
        elif char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    sorted_chars = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
    for i in range(5):
        print(f"{sorted_chars[i][0]}: {sorted_chars[i][1]}")
        
        

