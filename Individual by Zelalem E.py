
# THIS PROGRAM IS DONE BY ZELALEM ENYEW
tallies = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}
    # A FUNCTION USED TO CONVERT ROMAN TO DECIMAL
    # BY SUMMING UP THE NUMBERS
def RomanToDecimal(romanNumeral):
    sum = 0
    for i in range(len(romanNumeral) - 1):
        left = romanNumeral[i]
        right = romanNumeral[i + 1]
        if tallies[left] < tallies[right]:
            sum -= tallies[left]
        else:
            sum += tallies[left]
    sum += tallies[romanNumeral[-1]]

    if sum >3999:
        return print("Number is greater than 3999")
    else:
        return sum

print("-----------------------------------------------------------")
print("THIS PROGRAM CONVERTS ROMAN NUMBERS INTO DECIMAL NUMBERS!")
print("'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000,")
print("                 Done By: ZELALEM ENYEW                  ")
print("-----------------------------------------------------------")

while 1:
    FLAG = 0
    try: 
        print("Enter any roman number from 1 to 3999")
        roman = input()
        if len(roman) <= 3:
            print(roman," = ",RomanToDecimal(roman))
        elif len(roman)>3:
            for i in range(0,len(roman),1):
                if i>=3:
                    #A CODE USED TO HANDLE MORE THAN 3 CONSICUTIVE ROMAN NUMBERS
                    if roman[i] == roman[i-1] == roman[i-2] == roman[i-3]: 
                        FLAG=1
                        break

        if FLAG == 0:
            print(roman," = ",RomanToDecimal(roman))
            FLAG=0
        else:
            print("MORE THAN 3 TIMES ONE ROMAN NUMBER IS CONSECUTIVELY USED")
            FLAG=0
    except:
        print("Error!, Please give roman number only by using I,V,X,L,C,D,M")
    finally:
        print("------------------------------------------------------------")

