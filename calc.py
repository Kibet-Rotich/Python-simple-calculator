#ASBEL KIBET ROTICH
#SCT211-0087/2022
print("This is a simple calculator")
name = input("Greetings, my name is calculator what is your name? ")#GREETINGS
print("Hi,"+name+" you have a wonderful name.")
print("You will be prompted to enter a number kindly do so")
firstNumber = input("Enter the first number: ")#first number input
print("you will be prompted to enter an operator for the calculations you'd like me to perform")
print("+ for sum, - for subtraction, / for division and x for multiplication ")
operator = input("Enter operator: ")#operator input
print("You will now be prompted to enter the second number")
secondNumber = input("Enter the second number: ")#second number input

if (operator == "+"):#if else statement control structure
    print("The sum of the two numbers is equal to ", int(firstNumber)+int(secondNumber))
elif (operator == "-"):
  print("the difference between the first and second number is : ",int(firstNumber)-int(secondNumber))
elif(operator == "/"):
   print ("first number divided by the second number is :",int(firstNumber)/int(secondNumber))
elif(operator == "x"):
   print("first number multiplied by second number gives: ",int(firstNumber)*int(secondNumber))
else:
   print("An error occured!!!")
     
