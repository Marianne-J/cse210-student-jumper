# here goes the class for the puzzle

class Puzzle:
  
    def __init__(self):
        self.word = ""
        self.correct_letters = []
        
    def check_letter(self, guess):
        """ checks if a guess is both valid and in the puzzle's word.
        if both are true, the letter is added to the list of correct letters

        Args:
            guess - str: taken from the console. Should only be one letter

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
            List
        """
        current_word = []
        still_missing = True

        for word_letter in self.word:
            for correct_letter in self.correct_letters:

                if correct_letter.lower() == word_letter:
                    current_word.append(word_letter)
                    still_missing = False
                    break

                else:
                    still_missing = True

            if still_missing:
                current_word.append('_')

        return current_word