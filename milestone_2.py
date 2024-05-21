import random

word_list = ['Lychee', 'Mango', 'Papaya', 'Orange', 'Guava']
print(word_list)

random_word_pick = random.choice(word_list)
print(random_word_pick)

user_guess = input("Enter a single letter: ")
if user_guess.isalpha() == True and len(user_guess) == 1:
    print("Good guess!")
else:
    print("Oops! That is not a valid input")