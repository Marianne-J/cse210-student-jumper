import random

class Puzzle:
  
    def __init__(self):
        self.word = self.get_word_from_file().replace('\n', '')
        self.correct_letters = []

    def get_word_from_file(self):
        """Parses a .txt file of words, selects a random word from the list, and returns 
        the selected word.

        Args:
            self (Puzzle): An instance of Puzzle.

        Returns:
            String (Word): randomly chosen word
        """

        with open("jumper/game/words.txt", mode="rt") as word_file:
            file = word_file.readlines()
            file_length = len(file)
            word = file[random.randint(0, file_length)]

            return word
            
    def check_letter(self, guess):
        """ checks if a guess is both valid and in the puzzle's word.
        if both are true, the letter is added to the list of correct letters

        Args:
            String (guess): taken from the console. Should only be one letter

        Returns:
            Bool: if the guessed letter is found in the word
        """

        if len(guess) == 1:

            if guess.lower() in self.word:
                self.correct_letters.append(guess)
                return True
            else:
                return False
                
        else:
            print("error! You can only guess one letter at a time.")
            return False

    def get_current_word(self):
        """Keeps track of which letters are currently hidden and revealed.

          Args:
            self (Puzzle): An instance of Puzzle.
          Returns:
            String (current_word): The text to be displayed to the user
        """
        current_word_list = []
        still_missing = True

        for word_letter in self.word:
            for correct_letter in self.correct_letters:

                if correct_letter.lower() == word_letter:
                    current_word_list.append(word_letter)
                    still_missing = False
                    break

                else:
                    still_missing = True

            if still_missing:
                current_word_list.append('_')
        
        current_word = ""
        for letter in current_word_list:
            current_word += letter

        return current_word