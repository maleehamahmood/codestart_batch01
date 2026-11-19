"""
==============================================================
 BioSkillz CodeStart — Python Foundations | Batch 01
 Task 01: Variables, Data Types, Input, Operators & Typecasting
==============================================================

 Name     : ____________________

 Save as  : yourname_task_01.py   (example: ali_task_01.py)
 Deadline : Friday, 20 November 2026, 9:00 PM (PKT)
 Submit   : Upload this file to YOUR OWN GitHub repository.

 How to use this file
 --------------------
 1. Write your code below each "# Your code here" line.
 2. Run the file in VS Code and check your output against
    the example output given with each task.
 3. Make sure the whole file runs without errors before
    you upload it.

 Stuck? Share a screenshot of your code and the error in the
 CodeStart discussion group. Mistakes are part of learning.

 Empowering Skills | Lead with Science
"""


# ==============================================================
# PART A: SESSION EXERCISES
#
# The exercise questions are in the Session 01 recording.
# Watch the video, note down Exercises 1, 2 and 3, and solve
# them here.
#
# Session 01 recording (YouTube playlist): https://youtube.com/playlist?list=PLOMPeCDSq-kc&si=uY9I27bFj8yUqc00
# ==============================================================

# --------------------------------------------------------------
# Exercise 1
# --------------------------------------------------------------

# Your code here
print(7/2)
print(7//2)
print("7" + "2")
print(type(7.0))
print(2+3*4**2)
print(bool("0"))

# --------------------------------------------------------------
# Exercise 2
# --------------------------------------------------------------

# Your code here
Name = input("Name: ")
print("Hello " + Name)
age = int(input("Age: "))
print("Next year", age + 1)
print("Done")

# --------------------------------------------------------------
# Exercise 3
# --------------------------------------------------------------

# Your code here
Total = input("Total bill: ")
Friends = input("Number of friends: ")
print("Each pays: " + str(float(Total) / float(Friends)))
print("Left over: " + str(float(Total) % float(Friends)))

# ==============================================================
# PART B: TASKS
# ==============================================================

# --------------------------------------------------------------
# Task 1: Variables and Data Types
#
# Create four variables about yourself:
#   - your name   (string)
#   - your age    (integer)
#   - your height in metres (float)
#   - whether you are a student (boolean)
#
# Print each value along with its data type using type().
# Add at least one comment explaining your code.
#
# Example output:
#   Ali <class 'str'>
#   22 <class 'int'>
#   1.75 <class 'float'>
#   True <class 'bool'>
# --------------------------------------------------------------

# Your code here
Name = "Maleeha"
Age = 25
Height = 1.57
IsStudent = True

print(Name, type(Name)) #name will be printed along with data type, no input required since name given
print(Age, type(Age))
print(Height, type(Height))
print(IsStudent, type(IsStudent))

# --------------------------------------------------------------
# Task 2: Temperature Converter (Input and Typecasting)
#
# Ask the user to enter a temperature in Celsius.
# Convert the input to a float, then calculate and print the
# temperature in Fahrenheit and in Kelvin.
#
#   Fahrenheit = (Celsius * 9 / 5) + 32
#   Kelvin     = Celsius + 273.15
#
# Example output:
#   Enter temperature in Celsius: 37
#   Fahrenheit: 98.6
#   Kelvin: 310.15
# --------------------------------------------------------------

# Your code here
print(input("Enter temperature in Celsius: "))
Celsius = float(input("Enter temperature in Celsius: "))
Fahrenheit = (Celsius * 9 / 5) + 32
Kelvin = Celsius + 273.15
print("Fahrenheit: " + str(Fahrenheit))
print("Kelvin: " + str(Kelvin))

# --------------------------------------------------------------
# Task 3: Simple Calculator (Arithmetic Operators)
#
# Ask the user to enter two numbers and convert them to floats.
# Print the result of each of these operations:
#   addition, subtraction, multiplication, division,
#   floor division, modulus and exponent (power)
#
# Example output:
#   Enter first number: 17
#   Enter second number: 5
#   Addition: 22.0
#   Subtraction: 12.0
#   Multiplication: 85.0
#   Division: 3.4
#   Floor division: 3.0
#   Modulus: 2.0
#   Power: 1419857.0
# --------------------------------------------------------------

# Your code here
Number1 = float(input("Enter first number: "))
Number2 = float(input("Enter second number: "))
print("Addition: " + str(Number1 + Number2))
print("Subtraction: " + str(Number1 - Number2))
print("Multiplication: " + str(Number1 * Number2)) 
print("Division: " + str(Number1 / Number2))
print("Floor division: " + str(Number1 // Number2))
print("Modulus: " + str(Number1 % Number2))
print("Power: " + str(Number1 ** Number2))   

# --------------------------------------------------------------
# Task 4: Savings Tracker (Assignment Operators)
#
# Start with a variable: savings = 1000
# Then update it step by step using assignment operators
# (+=, -=, *=), printing the new value after each step:
#   1. You receive 500 as a gift          (use +=)
#   2. You spend 300 on books             (use -=)
#   3. Your savings double by year end    (use *=)
#
# Example output:
#   Starting savings: 1000
#   After gift: 1500
#   After buying books: 1200
#   After doubling: 2400
# --------------------------------------------------------------

# Your code here
print(input("Starting savings: 1000"))
savings = 1000
savings += 500
print("After gift: " + str(savings))
savings -= 300
print("After buying books: " + str(savings))
savings *= 2
print("After doubling: " + str(savings))

# --------------------------------------------------------------
# Task 5: Scholarship Check (Comparison and Logical Operators)
#
# A student qualifies for a scholarship if:
#   - their marks are 80 or more, AND
#   - their attendance is 75% or more
#
# Ask the user for their marks and attendance (convert both to
# integers). Then print True or False for each check below.
# Do not use if statements; use comparison and logical
# operators only.
#
# Example output:
#   Enter your marks: 85
#   Enter your attendance percentage: 70
#   Marks 80 or more: True
#   Attendance 75% or more: False
#   Qualifies for scholarship: False
# --------------------------------------------------------------

# Your code here
marks = int(input("Enter your marks: "))
attendance = int(input("Enter your attendance percentage: "))
print("Marks 80 or more: " + str(marks >= 80))
print("Attendance 75% or more: " + str(attendance >= 75))   
print("Qualifies for scholarship: " + str(marks >= 80 and attendance >= 75))

# ==============================================================
# Before you submit, check that:
#   [ ] Your name is written at the top of this file
#   [ ] The file is saved as yourname_task_01.py
#   [ ] The whole file runs without errors
#   [ ] Your output matches the examples
# ==============================================================
