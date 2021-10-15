# here goes the class for the jumper itself

class Jumper:

    def cut_line(self):
        self.mistakes += 1

        return self.mistakes

    def current_jumper(self):
        current_jumper = ['  ___  ', ' /___\\ ', ' \\   / ', '  \\ /  ', '   0   ', '  /I\\  ', '  / \\  ', '', '^^^^^^^']

        return current_jumper

    def get_current_jumper(self):
        visual = ""
        for x in range(self.mistakes, len(self.current_jumper)):
            visual += self.current_jumper[x]

        return visual
