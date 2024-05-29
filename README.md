# Hangman

# Table of Contents
1. [Introduction](#introduction)
    - [About the project](#About-the-project)
    - [Motivation for project](#Motivation-for-project)
    - [Topics covered](#Topics-covered)
2. [Features](#features)
    - [User Interaction](#User-Interaction)
    - [Lives Management](#Lives-Management)
    - [Feedback Managment](#Feedback-Managment)
    - [Example of game interaction](#Example-of-game-interaction)
    - [Game ending](#Game-ending)
3. [Installation instructions](#Installation-instructions)
4. [Usage instructions](#Usage-instructions)
5. [File structure](#File-structure)
6. [License information](#License-information)

## Introduction

### About the project
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts. This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

### Motivation for project
This project was created to apply the Python skills acquired during the AiCore bootcamp.

### Topics covered 
- Python basics and advanced
- imports
- class creation
- using the __init__ method to initialise attributes
- creating methods

## Features 
- Randomly selects a word from a predefined list for each game.
- Tracks the number of lives the player has.
- Checks validity of user guesses and provides appropriate feedback.
- Updates the display to show correctly guessed letters and their positions.
- Notifies the player of incorrect guesses and reduces the number of lives accordingly.
- Displays game ending 

### User Interaction
Prompt the user to guess a letter.

### Lives Management
The game starts with the player having 5 lives. Each incorrect guess reduces the number of lives by one.

### Feedback Managment
- Correct Guess: If the guessed letter is in the word, the player is informed of the correct guess, and the word display is updated to show the guessed letter in the correct positions.
- Incorrect Guess: If the guessed letter is not in the word, the player is informed of the incorrect guess, and the number of lives is decremented.
- Repeated Guess: If the letter has already been guessed, the player is notified that they have already tried that letter.

### Example of game interaction
```
Please guess a letter: p
Sorry, p is not in the word.
You have 4 lives left.
Your word so far : ['_', '_', '_', '_', '_', '_']
Please guess a letter: l
Good guess! l is in the word.
Your word so far : ['l', '_', '_', '_', '_', '_']
Please guess a letter: l
You already tried that letter!
```

### Game ending
- If you guess the word correctly:
```
Congratulations. You won the game!
```
- If you lose all your lives:
```
You lost!
The word was: papaya
``` 

## Installation instructions
You are able to start the game locally in your machine by typing the following commands in the command line:
`git clone URL`
- Basic Python installation required. 
- No special libraries needed.

## Usage instructions
1. Execute the Python script to start the game. 
   `Python milestone_5.py`
2. Change the words on word list as required
   ```Python
   word_list = ['word_1', 'word_2', 'word_3', 'word_4', 'word_4']
   ```

## File structure
hangman/milestone_5.py - The main Python file that's responsible for running the game's logic

## License information
Distributed under the MIT License. See LICENSE for more information.

