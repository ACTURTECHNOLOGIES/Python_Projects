greet= input("Hello welcome to my app, what's your name: ")
print ("Hello " + greet)

user_input=(input("This is a calculator what operation do you want e.g addition: "))



if user_input=='addition':
    x=input("Enter your first number: ")
    y=input("Enter your second number: ")
    sum = int(x) + int(y)
    print (greet +" your result is " +str(sum))


if user_input=='subtraction':
    x=input("Enter your first number: ")
    y=input("Enter your second number: ")
    sum = int(x) - int(y)
    print ("David your result is " +str(sum))

if user_input=='Division':
    x=input("Enter your first number: ")
    y=input("Enter your second number: ")
    sum = int(x) / int(y)
    print ("David your result is " +str(sum))

if user_input=='Multiplication':
    x=input("Enter your first number: ")
    y=input("Enter your second number: ")
    sum = int(x) * int(y)
    print ("David your result is " +str(sum))

if user_input=='Modulo':
    x=input("Enter your first number: ")
    y=input("Enter your second number: ")
    sum = int(x) % int(y)
    print ("David your result is " +str(sum))

