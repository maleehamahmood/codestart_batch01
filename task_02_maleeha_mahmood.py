"""
==============================================================
 BioSkillz CodeStart — Python Foundations | Batch 01
 Task 02: Strings & Conditional Statements
==============================================================

 Name     : Maleeha Mahmood

 Save as  : yourname_task_02.py   (example: ali_task_02.py)
 Deadline : Friday, 20 November 2026, 9:00 PM (PKT)
 Submit   : Upload this file to YOUR OWN GitHub repository.

 How to use this file
 --------------------
 1. Write your code below each "# Your code here" line.
 2. Run the file in VS Code and check your output against
    the example output given with each task.
 3. Make sure the whole file runs without errors before
    you upload it.

 Tip: These tasks also use what you learned in Session 01,
 such as input(), typecasting and operators.

 Stuck? Share a screenshot of your code and the error in the
 CodeStart discussion group. Mistakes are part of learning.

 Empowering Skills | Lead with Science
"""


# ==============================================================
# PART A: SESSION EXERCISES
#
# The exercise questions are in the Session 02 recording.
# Watch the video, note down Exercises 1, 2 and 3, and solve
# them here.
#
# Session 02 recording (YouTube playlist): https://youtube.com/playlist?list=PLOMPeCDSq-kc&si=uY9I27bFj8yUqc00
# ==============================================================

# --------------------------------------------------------------
# Exercise 1
# --------------------------------------------------------------

# Your code here
print("Python" [1:4])
print("banana".count("an"))
print("Hello" [-1])
print("Zebra"<"apple")
print(5>3 and 2>4)
print(not " ")

# --------------------------------------------------------------
# Exercise 2
# --------------------------------------------------------------

# Your code here
marks = int(input("Enter your marks: "))
if marks >= 50:
      print("Pass")
else:
      print("Fail")
answer = input("Again?")
if answer == "yes":
     print("Restarting...")

# --------------------------------------------------------------
# Exercise 3
# --------------------------------------------------------------

# Your code here
print(input("Name: "))
marks = int(input("Enter your marks: "))
if marks >= 90:
      print("A")
elif marks >= 80:
      print("B")
elif marks >= 70:
      print("C")
elif marks >= 50:
      print("D")
else:
      print("F")

# ==============================================================
# PART B: TASKS
# ==============================================================

# --------------------------------------------------------------
# Task 1: Name Formatter (String Methods)
#
# Ask the user to enter their full name. Then print:
#   - the name in uppercase          (use upper())
#   - the name in lowercase          (use lower())
#   - the name in title case         (use title())
#   - the total number of characters, including spaces (use len())
#   - how many times the letter "a" appears (use count())
#
# Example output:
#   Enter your full name: ayesha khan
#   Uppercase: AYESHA KHAN
#   Lowercase: ayesha khan
#   Title case: Ayesha Khan
#   Total characters: 11
#   Number of 'a': 3
# --------------------------------------------------------------

# Your code here
name = input("Name: ")
print("Uppercase: " + name.upper())
print("Lowercase: " + name.lower())
print("Title case: " + name.title())
print("Total characters: " + str(len(name)))
print("Number of 'a': " + str(name.count("a")))

# --------------------------------------------------------------
# Task 2: Email Breakdown (Indexing and Slicing)
#
# Ask the user to enter an email address. Then print:
#   - the first character               (use indexing)
#   - the last character                (use negative indexing)
#   - the position of "@"               (use find())
#   - the username, the part before "@" (use slicing)
#   - the domain, the part after "@"    (use slicing)
#   - whether it is a Gmail address     (use endswith())
#
# Hint: Save the position of "@" in a variable first, then use
# it inside your slices.
#
# Example output:
#   Enter your email: ali.khan@gmail.com
#   First character: a
#   Last character: m
#   Position of @: 8
#   Username: ali.khan
#   Domain: gmail.com
#   Gmail address: True
# --------------------------------------------------------------

# Your code here
email = input("Enter your email: ")
print("First character: " + email[0])
print("Last character: " + email[-1])
print("Position of @: " + str(email.find("@")))
print("Username: " + str(email[0:email.find("@")]))
print("Domain: " + str(email[email.find("@")+1:]))
print("Gmail address: " + str(email.endswith("gmail.com")))

# --------------------------------------------------------------
# Task 3: Report Card (f-strings and Typecasting)
#
# Ask the user for their name and their marks in three
# subjects, each out of 100. Convert the marks to floats.
# Calculate the total and the percentage, then print a short
# report using f-strings. Show the percentage with exactly
# 2 decimal places.
#
#   Percentage = (Total / 300) * 100
#
# Hint: {percentage:.2f} shows a number with 2 decimal places.
#
# Example output:
#   Enter your name: Sara
#   Enter marks for Subject 1: 78
#   Enter marks for Subject 2: 85.5
#   Enter marks for Subject 3: 90
#   ----- Report Card -----
#   Name: Sara
#   Total: 253.5 out of 300
#   Percentage: 84.50%
# --------------------------------------------------------------

# Your code here
name = input("Enter your name: ")
mark1=float(input ("Enter marks for Subject 1: "))
mark2=float(input ("Enter marks for Subject 2: "))
mark3=float(input ("Enter marks for Subject 3: "))
Total=mark1+mark2+mark3
Percentage=(Total/300)*100
print("----- Report Card -----")
print("Name: " + name)
print("Total: " + str(Total) + " out of 300")
print("Percentage: {:.2f}%".format(Percentage))

# --------------------------------------------------------------
# Task 4: Grade Calculator (if, elif and else)
#
# Ask the user to enter their marks (0 to 100) and convert them
# to an integer. Print their grade using this scale:
#
#   85 to 100  ->  A
#   70 to 84   ->  B
#   55 to 69   ->  C
#   40 to 54   ->  D
#   0 to 39    ->  F
#
# If the marks are below 0 or above 100, print "Invalid marks".
#
# Hint: Check for invalid marks first.
#
# Example output 1:
#   Enter your marks: 72
#   Grade: B
#
# Example output 2:
#   Enter your marks: 105
#   Invalid marks
# --------------------------------------------------------------

# Your code here
marks = int(input("Enter your marks: "))
if marks < 0 or marks > 100:
      print("Invalid marks")
elif marks >= 85 and marks <= 100:
      print("Grade: A")
elif marks >= 70 and marks <= 84:
      print("Grade: B")
elif marks >= 55 and marks <= 69:
      print("Grade: C")
elif marks >= 40 and marks <= 54:
      print("Grade: D")
else:
      print("Grade: F")

# --------------------------------------------------------------
# Task 5: Login Checker (Nested Conditions)
#
# The correct login details are:
#   username: codestart
#   password: python123
#
# Ask the user for a username and a password.
#   - The username should NOT be case-sensitive, and extra
#     spaces should be ignored. (Use strip() and lower().)
#   - The password IS case-sensitive.
#
# Use a nested if statement:
#   - If the username is correct, check the password:
#       correct password -> "Login successful. Welcome to CodeStart!"
#       wrong password   -> "Incorrect password. Please try again."
#   - If the username is wrong -> "Username not found."
#
# Example output 1:
#   Enter username:   CodeStart
#   Enter password: python123
#   Login successful. Welcome to CodeStart!
#
# Example output 2:
#   Enter username: codestart
#   Enter password: Python123
#   Incorrect password. Please try again.
#
# Example output 3:
#   Enter username: student
#   Enter password: python123
#   Username not found.
# --------------------------------------------------------------

# Your code here
username = input("Enter username: ").strip().lower()
password = input("Enter password: ")
if username == "codestart":
      if password == "python123":
            print("Login successful. Welcome to CodeStart!")
      else:
            print("Incorrect password. Please try again.")
else:
      print("Username not found.")

# ==============================================================
# Before you submit, check that:
#   [ ] Your name is written at the top of this file
#   [ ] The file is saved as yourname_task_02.py
#   [ ] The whole file runs without errors
#   [ ] Your output matches the examples
# ==============================================================
