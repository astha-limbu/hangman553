import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        ''' Initializes the Hangman game with a list of words and number of lives.'''
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word] # A list of the letters of the word, with _ for each letter not yet guessed
        self.num_letters = len(set(self.word)) # The number of UNIQUE letters in the word that have not been guessed yet
        self.list_of_guesses = [self.word_guessed] # A list of the guesses that have already been tried
    
    def check_guess(self, guess):
        '''
        Checks if the guessed letter is in the word and updates the game state.
        Reveals the guessed letter in the word_guessed list
        '''
        guess = guess.lower()
        if guess in self.word:
            self.num_letters -= 1
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        print(f"Your word so far : {self.word_guessed}")
        print(self.num_letters)

    def ask_for_input(self):
        '''
        Prompts the user to guess a letter. 
        Validates the guessed letter.
        '''
        while True: 
            guess = input("Please guess a letter: ").lower()
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
            break

def play_game(word_list):
    ''' Starts the Hangman game and continues until the player wins or loses.'''
    game = Hangman(word_list, num_lives = 5)    
    while True:
        if game.num_lives == 0:
            print("You lost!")
            print(f"The word was: {game.word}")
            break
        elif game.num_letters == 0:
            print("Congratulations. You won the game!")    
            break
        else:
            game.ask_for_input()
            


if __name__ == '__main__':
    word_list = ['lychee', 'mango', 'papaya', 'orange', 'guava']
    play_game(word_list)