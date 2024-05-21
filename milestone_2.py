import random

word_list = ['Lychee', 'Mango', 'Papaya', 'Orange', 'Guava']
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Enter a single letter: ")
if guess.isalpha() == True and len(guess) == 1:
    print("Good guess!")
else:
    print("Oops! That is not a valid input")