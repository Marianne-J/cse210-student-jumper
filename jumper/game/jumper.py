class Jumper:
    
    def __init__(self):
        self.mistakes = 0
        self.current_jumper = ["  ___  ", " /   \ ", "  ___  ", " \   / ", "  \ /  ", "   0   ", "  /|\  ", "  / \  ", "       ", "^^^^^^^"]

    def cut_line(self):
        self.mistakes += 1

    def get_current_jumper(self):
        visual = ""
        for x in range(self.mistakes, len(self.current_jumper)):
            visual += self.current_jumper[x]

        return visual