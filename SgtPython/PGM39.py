vowels = "aeiou"
words = input("Enter string")
vowel = 0
consonant = 0
number = 0
special_character = 0
for i in words:
    if i.isdigit():
        number += 1
    elif i.lower() in vowels:
        vowel += 1
    elif i.isalpha():
        consonant += 1
    else:
        special_character += 1
print('Vowel Count:', vowel)
print('Consonant Count:', consonant)
print('Number Count:', number)
print("SpecialCharacter Count", special_character)
