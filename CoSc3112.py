import re
import itertools as it

romans = {
   'I' : 1,   
   'V' : 5,   
   'X' : 10,  
   'L' : 50,  
   'C' : 100,  
   'D' : 500, 
   'M' : 1000,
   # The Basic Roman Numbers
}

# A functio to conver roman number into decimal equivalent

def RomanNumeralToDecimal(romanNumeral):
    sum = 0
    i   = 0
    while (i < len(romanNumeral) ):
      
          
            left = romanNumeral[i]
            if (i + 1 < len(romanNumeral)):

               right = romanNumeral[i + 1]
               
               if romans[left] >= romans[right]:
                     sum += romans[left]
                     i   += 1 

               else:
                     sum = sum + romans[right] - romans[left]
                     i  += 2
                      
            
            else:      
              sum += romans[left]
              i   += 1
              
      
    return sum

# Open a file 
text = open("txt.txt", "r") 
txt = text.read().lower()

#A function to remove meaningless characters

def remove_punc_and_special_chars(): 
        normalized_text = re.sub('[0-9\!\@\#\$\%\^\«\»\&\*\(\)\…\[\]\{\}\;\“\”\›\’\‘\"\'\:\,\.\‹\/\<\>\?\\\\|\`\´\~\-\=\+\፡\።\፤\;\፦\፥\፧\፨\፠\፣]', '',txt) 
        return normalized_text

#A function to compute a word frequency from the txt file 
def word_Frequency():
     frequency = {}
     txt_word = re.findall(r'\b[a-z]{2,15}\b', txt)
     for word in txt_word:
        count = frequency.get(word,0)
        frequency[word] = count + 1
        sortedfrequency = sorted(frequency.items(), key=lambda x:x[1], reverse=True)
        word_frequency = dict(sortedfrequency)
        frequency_list_word = word_frequency.keys()
     print("====================================================================================================================") 
     for words in frequency_list_word:
          print(words,'=',word_frequency[words])
     print("====================================================================================================================")
     
    
#A function to compute the firs five most frequent charcters from the txt file              
def char_Frequency():
     frequency = {}
     txt_char = re.sub('[\s]','',txt)
     for char in txt_char:
          count = frequency.get(char,0)
          frequency[char] = count + 1
          sortedfrequency = sorted(frequency.items(), key=lambda x:x[1], reverse=True)
          char_frequency = dict(sortedfrequency)
          frequency_list_char = dict(it.islice(char_frequency.items(), 5))
     print("====================================================================================================================")  
     for chars in frequency_list_char: 
         print(chars,'=',char_frequency[chars])
     print("====================================================================================================================")
             
#A function to Display overall information of the txt file
def stasticalInformation():
     
     with open("txt.txt", 'r') as txt:
         total_lines = 0
         for line in txt:
              if line.rstrip():
                   total_lines += 1
         txt_read = txt.read()          
     print("====================================================================================================================")  
     print("The total number of lines:", total_lines)
     txt_read = remove_punc_and_special_chars()
     txt_char = re.sub('[\s]','',txt_read)
     total_characters = len(txt_read)
     word = txt_read.split()
     total_words = len(word)   
     print("The total number of words:", total_words)
     print("The total number of characters:", total_characters)
     print("====================================================================================================================")
     txt.close()


#*******************************************GET STARTED******************************************************************
print("====================================================================================================================")
str = input("Wellcome to Python Mini Project By: Wendmagegn Sisay (ID): 1233/12, (To): Derbew F.\n Pls hit Enter to Continue...... ")      
print("====================================================================================================================")
txt = remove_punc_and_special_chars()


while (str != '0'):
     
     flag = 0
     i     = 0
     if (str == ''):
          print("====================================================================================================================")   
          str = input ("******* Pls Select an Option for Computation *******\n1====== For Roman to Decimal number Conversion ======\n2====== For Word Frequency Computation ======\n3====== For Charcter Frequency Computation ======\n4====== For Stastical Informations ======\n0****** For Exit!!! ******\n ")    
          print("====================================================================================================================")      
     elif (str == '1'):
          print("====================================================================================================================")   
          inp = input("Insert a Roman Number 1 upto 3999, OR 0 to Back to Main_Menu!!!\n")
          print("====================================================================================================================")  
          if (inp.isalpha()):
       
             romanNumeral = inp.upper()
        
             D = romanNumeral.count('D')
         
             L = romanNumeral.count('L')
         
             V = romanNumeral.count('V')
        
      
             if ( L > 1 or V > 1 or  D > 1 ):
       
               flag = 1


         
             try:
               for i in range(len(romanNumeral)):
               
                    if (i + 3 < len(romanNumeral)):       
                         if(romans[romanNumeral[i]] == romans[romanNumeral[i + 1]] == romans[romanNumeral[i + 2]] == romans[romanNumeral[i + 3]]):
                              flag = 1     
                    if (i + 4 < len(romanNumeral)):
                         if(romans[romanNumeral[i]] >= romans[romanNumeral[i + 1]] == romans[romanNumeral[i + 2]] == romans[romanNumeral[i + 3]] == romans[romanNumeral[i + 4]]):
                              flag = 1    
                    if (i + 5 < len(romanNumeral)):
                         if(romans[romanNumeral[i]] >= romans[romanNumeral[i + 1]] >= romans[romanNumeral[i + 2]] == romans[romanNumeral[i + 3]] == romans[romanNumeral[i + 4]] == romans[romanNumeral[i + 5]]):
                              flag = 1
                    if (i + 6 < len(romanNumeral)):
                         if(romans[romanNumeral[i]] >= romans[romanNumeral[i + 1]] >= romans[romanNumeral[i + 2]] >= romans[romanNumeral[i + 3]] == romans[romanNumeral[i + 4]] == romans[romanNumeral[i + 5]] == romans[romanNumeral[i + 6]]):
                              flag = 1            
                    if (i + 7 < len(romanNumeral)):   
                         if(romans[romanNumeral[i]] >= romans[romanNumeral[i + 1]] >= romans[romanNumeral[i + 2]] >= romans[romanNumeral[i + 3]] >= romans[romanNumeral[i + 4]] == romans[romanNumeral[i + 5]] == romans[romanNumeral[i + 6]] == romans[romanNumeral[i + 7]]):
                              flag = 1    
             except:
                    print("====================================================================================================================")
                    print("The Number is not Recognized, Error!!!")
                    print("====================================================================================================================")
                            

             if (flag == 1):
                 print("====================================================================================================================")   
                 print("The Number is not Recognized, Error!!!")
                 print("====================================================================================================================")  
                 flag = 0 
         
             else:

                    try:
            
                         decimal = RomanNumeralToDecimal(romanNumeral)

                    except:
                         print("====================================================================================================================")                 
                         print("Undefined Input, pls try again!!! ")
                         print("====================================================================================================================")
                    else:
                         print("====================================================================================================================")     
                         print ("The Roman Number : " +romanNumeral +" is", decimal, " in Decimal")
                         print("====================================================================================================================")


          elif (inp == '0'):
               str = ''
          
          else:
               print("====================================================================================================================")   
               print("Pls Insert only Roman Numerics, Error!!!")
               print("====================================================================================================================") 
               str = '1'      
   
      
     elif (str == '2'):
          word_Frequency()
          str = ''
             
     elif (str == '3'):
          char_Frequency()
          str = ''
             
     elif (str == '4'):
          stasticalInformation()
          str = ''
             
     elif (str == '0'):
          break

     else:
          print("====================================================================================================================")
          print("Error, try again!!!")
          print("====================================================================================================================")    
          str = ''
         

text.close()