# Name: SABIRIL RAUF
# NIM: 2611532023
# Question 3a
text = "Informatika"
print(text[10]) 
print(text.upper())
print(text[0:11])

#queston 3b
text = "sabiril rauf"
count = 0
for char in text.lower():
    if char in "aiueo":
        count += 1
print("Vowels:", count)
