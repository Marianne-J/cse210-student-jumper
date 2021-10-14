# here goes the class for the jumper itself

class Jumper:
  
  
    def get_current_jumper(self):
        visual = ""
        for x in range(self.mistakes, len(self.current_jumper)):
            visual += self.current_jumper[x]

        return visual

    def get_current_word():
        """Keeps track of which letters are currently hidden and revealed.

          Args:
            self (Puzzle): An instance of Puzzle.
          Returns:
            List
        """
        current_word = []
        still_missing = True

        for word_letter in word:
            for correct_letter in correct_letters:

                if correct_letter.lower() == word_letter:
                    current_word.append(word_letter)
                    still_missing = False
                    break

                else:
                    still_missing = True

            if still_missing:
                current_word.append('_')

        return current_word