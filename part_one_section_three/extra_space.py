"""

Your friend is working on an app for job seekers

The program should print out exactly the following:

my name is Tim Tester, I am 20 years old

my skills are
 - python (beginner)
 - java (veteran)
 - programming (semiprofessional)

I am looking for a job with a salary of 2000-3000 euros per month



"""

name = "Tim Tester"

age = 20

skill_one = "python"
level_one = "beginner"
skill_two = "java"
level_two = "veteran"
skill_three = "programming"
level_three = "semiprofessional"

lower = 2000

upper = 3000


print(f"my name is {name}, I am {age} years old")
print("")
print("my skills are")
print(f" - {skill_one} ({level_one})")
print(f" - {skill_two} ({level_two})")
print(f" - {skill_three} ({level_three})")
print("")
print(f"I am looking for a job with a salary of {lower}-{upper} euros per month")
