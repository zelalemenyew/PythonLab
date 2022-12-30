############################################################################
##################### GROUP TWO MEMBERS ONLY ###############################
############################################################################

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

    #######    string manipulation
x= "Abachada"
print(x[0:])

print (bin(60))

    #######    Typecasting
x = 4
print(type(4)) # at this moment, x points to an integer
x = "Hello, world"
print(type(x)) # and at this moment, x points to a string

    ###### Else if is translated into ilif

for x in range(101):
    if x%3==0 and x%5==0 :
        print(x,"Hello World")
    elif x%3==0 :
        print(x,"Hello")
    elif x%5==0 :
        print(x,"World")
    else :
        print(x)

fruits = [1,2,3,4,6,7,8,9]
for variable in fruits:
  print(variable)

   ###### SWITCH STATEMENT IN PYTHON #######
x = "Zol"
match x:
    case "Z":
        print("ZEE found")
    case "Zol":
        print("Oops!,Zolanchy found in")
    case other: ## case other is similar to "case _:""
        print("Not found")


