import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word] # A list of the letters of the word, with _ for each letter not yet guessed
        self.num_letter = len({self.word}) # The number of UNIQUE letters in the word that have not been guessed yet
        self.list_of_guesses = [self.word_guessed] # A list of the guesses that have already been tried
    
    # checks if the guess is in the word print a message saying "Good guess! {guess} is in the word."
    def check_guess(self, guess):
        # convert guessed letter to lowercase,
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

            # replace the corresponding "_" in the word_guessed with the guess
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess

            # reduce the number of unique letters left to guess
            self.num_letter -= 1
        
        # reduce life and show lives left
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        print(f"Your word so far : {self.word_guessed}")

    def ask_for_input(self):
        while True: # while loop and set the condition to True
            guess = input("Please guess a letter: ") # Ask the user to guess a letter

            # if the guess is NOT a single alphabetical character print a message saying "Invalid letter. Please, enter a single alphabetical character."
            if guess.isalpha() == False or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character")

            # if the guess is already in the list_of_guesses print a message saying "You already tried that letter!"
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")

            # If the guess is a single alphabetical character and it's not already in the list_of_guesses call the check_guess method
            else:
                self.check_guess(guess)
                #  append the guess to the list_of_guesses
                self.list_of_guesses.append(guess)

word_list = ['lychee', 'mango', 'papaya', 'orange', 'guava']
game = Hangman(word_list)
game.ask_for_input()
