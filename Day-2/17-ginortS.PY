string = input()
lower = sorted([letter for letter in string if letter.islower()])
upper = sorted([letter for letter in string if letter.isupper()])
odd = sorted([letter for letter in string if letter.isdigit() and int(letter) % 2])
even = sorted([letter for letter in string if letter.isdigit() and not int(letter) % 2])
print(''.join(lower + upper + odd + even))