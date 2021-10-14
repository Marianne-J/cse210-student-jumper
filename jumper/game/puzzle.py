# here goes the class for the puzzle

class Puzzle:
  
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