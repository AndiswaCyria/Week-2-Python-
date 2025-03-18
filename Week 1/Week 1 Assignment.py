num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: ") )
print("Which operation would you like to perform")
ch = input ("Enter any of these operations +,-,*,/: ")

result = 0 
if ch == '+':
    result = num1 + num2
elif ch == '-':
    result = num1 -num2
elif ch == '*':
    result = num1 *num2
elif ch == '/':
    result = num1 /num2

else:
    print ("Invalid Input")

print(num1, ch , num2, ":", result)       