sentence = "apa ini apa"

clean = sentence.replace(" ", "").lower()

if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")