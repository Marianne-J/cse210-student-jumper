# here goes the class for the jumper itself

class Jumper:

        pass

    def get_current_jumper(self):
        visual = ""
        for x in range(self.mistakes, len(self.current_jumper)):
            visual += self.current_jumper[x]

        return visual
