#PEMANASAN
first_name = " muhammad"
last_name = "rafi "
full_name = first_name.strip() + " " + last_name.strip()
print(full_name)
print(full_name.title())

# Name: SABIRIL RAUF
# NIM: 2611532023
# Question 6
full_name = "  Siti Aisyah  "
nim = "2610511023"

name = full_name.strip()
pos = name.find(" ")

if pos == -1:
    first_name = name
else:
    first_name = name [:pos]

username = first_name.lower()+nim[-3:]
print(username)