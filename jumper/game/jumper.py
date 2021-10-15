class Jumper:
    
    def __init__(self):
        self.mistakes = 0
        self.current_jumper = ["  ___  ", " /   \ ", "  ___  ", " \   / ", "  \ /  ", "   0   ", "  /|\  ", "  / \  ", "       ", "^^^^^^^"]

    def cut_line(self):
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