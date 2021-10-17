class Jumper:
    """A code template for a jumper for a word puzzle game. Keeps track of how many mistakes have been
    made and uses that to determine and return the current appearance of the jumper.

    Stereotype:
        GameObject

    Attributes:
        mistakes (int): the number of mistakes made
        current_jumper (List): list of strings used to form the display of the jumper
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.mistakes = 0
        self.current_jumper = ["  ___  ", " /   \ ", "  ___  ", " \   / ", "  \ /  ", "   0   ", "  /|\  ", "  / \  ", "       ", "^^^^^^^"]


    def cut_line(self):
        """Used by the director to increment the mistakes counter.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self.mistakes += 1

    def get_current_jumper(self):
        """Using current_jumper and a for loop, puts together a string to return to Director.
        The string is used to show the current state of the jumper.

        Args:
            self (Jumper): An instance of Jumper.
        Returns:
            string (visual): The current visual state of the jumper.
        """
        visual = ""
        for x in range(self.mistakes, len(self.current_jumper)):
            visual += self.current_jumper[x] + "\n"

        return visual