char = input("Enter a character: ").lower()

if len(char) != 1 or not char.isalpha():
    print("Please enter a single alphabet.")
elif char in "aeiou":
    print("It is a vowel")
else:
    print("It is a consonant")
