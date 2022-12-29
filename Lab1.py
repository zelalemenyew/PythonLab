print("Lets try to accept two numbers and sum upp them and display to the user")
print("Enter a first Number:")
accept1 = int(input())
print("Enter a second Number:")
accept2 = int(input())
print("The Sum is:",accept1+accept2)

###### ASCII VALUES ########
print("ASCII VALUE OF 'A':",ord("A"))


####### Format function: WAY ONE #######
Output = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
print(Output)

####### Format function: WAY TWO #######
Output2 = "My name is {:s}, I'm {:d}".format("CodeZEE",23)
print(Output2)
