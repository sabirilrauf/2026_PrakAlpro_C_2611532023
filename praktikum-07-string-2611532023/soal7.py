# Name: SABIRIL RAUF
# NIM: 2611532023
# Question 7
name = "sabiril rauf"
nim = "2611532023"

pos = name.find(" ")
if pos == -1:
    first_name = name
else:
    first_name = name[:pos]
username = first_name + nim[-3:]

# Angkatan dari NIM dengan slicing
intake = "20" + nim[:2]

print("=" * 30)
print("STUDENT CARD".center(30))
print("=" * 30)
print("Name".ljust(10) + ": " + name.title())
print("NIM".ljust(10) + ": " + nim)
print("Username".ljust(10) + ": " + username)
print("Intake".ljust(10) + ": " + intake)
print("=" * 30)