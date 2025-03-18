temperature = 20

if temperature > 25:
    print("It’s a hot day! ")
else:
    print("It’s a cool day!")

# Control flow example for grading student marks
# This will ask the user for input and grade the student's performance

# Prompt the user for student marks
marks = int(input("Enter the student's marks (0-100): "))

# Grading system based on the marks
if marks > 70:
    print("Grade: Distinction 🏆")
elif marks >= 60:
    print("Grade: Credit 🎖️")
elif marks >= 50:
    print("Grade: Pass 👍")
else:
    print("Grade: Fail ❌")



    #If-elif-else statements
    num = 10
    if num > 0:
        print("Positive number")
    elif num == 0:
        print("Zero")
    else:
        print("Negative number")

        #nested if statements
        if num % 2 == 0:
            print("Even number")
            if num > 0:
                print("Also positive!")
            else:
                print("Odd number")
