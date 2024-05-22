def check_guess(user_guess):
    user_guess = user_guess.lower()
    if user_guess in random_word_pick:
        print(f"Good guess! {user_guess} is in the word.")
    else:
        print(f"Sorry, {user_guess} is not in the word. Try again.")

def ask_for_input():
    user_guess = ""
    while True:
        user_guess = input("Please guess a letter: ")
        if user_guess.isalpha() == True and len(user_guess) == 1:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(user_guess)
ask_for_input()