import random

hangman = [['   _______    ',
            '  |           ',
            '  |           ',
            '  |           ',
            '  |           ',
            '/---\         '],
           ['   _______    ',
            '  |       |   ',
            '  |           ',
            '  |           ',
            '  |           ',
            '/---\         '],
           ['   _______    ',
            '  |       |   ',
            '  |       0   ',
            '  |           ',
            '  |           ',
            '/---\         '],
           ['   _______    ',
            '  |       |   ',
            '  |       0   ',
            '  |       |   ',
            '  |           ',
            '/---\         '],
           ['   _______    ',
            '  |       |   ',
            '  |       0   ',
            '  |      /|   ',
            '  |           ',
            '/---\         '],
           ['   _______    ',
            '  |       |   ',
            '  |       0   ',
            '  |      /|\  ',
            '  |           ',
            '/---\         '],
            ['   _______    ',
            '  |       |   ',
            '  |       0   ',
            '  |      /|\  ',
            '  |      /    ',
            '/---\         '],
            ['   _______    ',
            '  |       |   ',
            '  |       0   ',
            '  |      /|\  ',
            '  |      / \  ',
            '/---\         ']
            ]

allowed_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                       'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '*']

class Hangman:

    def __init__(self, word: str):
        self.word = word
        self.mistakes = 0
        self.hint = ['_'] * len(self.word)
        self.letter = ''
        self.used_letters = []

    #The method that starts the game
    def start_game(self):
        while self.mistakes < len(hangman) - 1:
            self.show_hint()
            self.input_letter()
            self.check_word()
        self.show_hint()
        print(f'Game Over. The word was "{self.word}".')
        self.end_game()

    #The method that shows the hangman art, the letters used and the hint (number of letters in the word
    # and the ones that were guessed)
    def show_hint(self):
        print('\n'.join(hangman[self.mistakes][:]))
        print(f"The letters that you have already used are: {', '.join(self.used_letters)}")
        print('The word: ' + ''.join(self.hint))

    #The method for user to guess a letter or the entire word
    def input_letter(self):
        self.letter = input('Please enter a letter (or * to guess the entire word): ').lower()
        if self.letter not in allowed_characters:
            print('Please enter a valid letter (or *).')
            self.input_letter()
        elif self.letter == '*':
            self.letter = input('You may guess the entire word: ').lower()
            if self.letter == self.word:
                print('Congratulations, you guessed the word!')
                self.end_game()
            else:
                print('Unfortunately, this letter is not the word.')
                self.mistakes += 1
                self.input_letter()
        else:
            if self.letter in self.hint or self.letter in self.used_letters:
                print('You have already used that letter. Pick a different one.')
                self.input_letter()

    #The method that checks whether a letter is in the word
    def check_word(self):
        self.used_letters.append(self.letter)
        if self.letter not in self.word:
            print('The letter is not in the word!')
            self.mistakes += 1
        else:
            print('The letter is in the word!')
            for index, name in enumerate(self.word):
                if name == self.letter:
                    self.hint[index] = self.letter
                    if self.hint == list(self.word):
                        print('Congratulations, you won!')
                        self.end_game()

    #The method that ends the game and inquires whether the player wants to play again
    def end_game(self):
        answer = input('Would you like to play again? (yes/no): ').lower()
        if answer == 'yes':
            word = random.choice(word_list)
            Hangman(word).start_game()
        elif answer == 'no':
            print('Thank you for playing!')
            exit()
        else:
            print('Please enter \'yes\' or \'no\'.')
            self.end_game()

if __name__ == '__main__':
    word_list = open('words.txt').read().split()
    word = random.choice(word_list)
    Hangman(word).start_game()