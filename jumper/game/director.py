from game.console import Console
from game.jumper import Jumper
from game.puzzle import Puzzle

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.

    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        jumper (Jumper): An instance of the class of objects known as Jumper.
        player (Player): An instance of the class of objects known as Player.
        keep_playing (boolean): Whether or not the game can continue.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.console = Console()
        self.jumper = Jumper()
        self.puzzle = Puzzle()
        self.keep_playing = True
        self.current_guess = ""
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.do_outputs()
            self.get_inputs()
            self.do_updates()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means receiving a guess from the player.

        Args:
            self (Director): An instance of Director.
        """
        self.current_guess = self.console.read("Guess a letter [a-z]: ")
        
        
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means the following:
            > Checking whether a line should be cut
            > Checking if the game has ended in a loss or victory

        Args:
            self (Director): An instance of Director.
        """

        if not self.puzzle.check_letter(self.current_guess):
            self.jumper.cut_line()

        if self.jumper.mistakes == 5:
            self.keep_playing = False

            for i in ["   x   ", "  /|\  ", "  / \  ", "       ", "^^^^^^^"]:
                self.console.write(i)

            self.console.write(f"The correct word was '{self.puzzle.word}'")
            self.console.write("You lost!! Better luck next time.")
        else:
            puzzle_solved = True

            for char in self.puzzle.get_current_word():
                if char == "_":
                    puzzle_solved = False
            
            if puzzle_solved:
                self.keep_playing = False
                self.console.enter()
                self.console.write("You correctly guessed the word! Congrats!")

        
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means displaying the current state of the puzzle and jumper

        Args:
            self (Director): An instance of Director.
        """
        self.console.enter()
        current_word = self.puzzle.get_current_word()
        self.console.write(current_word)

        self.console.enter()
        current_jumper = self.jumper.get_current_jumper()
        self.console.write(current_jumper)