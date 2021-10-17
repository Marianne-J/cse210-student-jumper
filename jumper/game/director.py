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
        that means moving the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        choice = self.console.read("Guess a letter [a-z]: ")

        if not self.puzzle.check_letter(choice):
            self.jumper.cut_line()
        
        
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means the hider watches the seeker.

        Args:
            self (Director): An instance of Director.
        """
        # updates go here
        
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means displaying the current state of the puzzle and jumper

        Args:
            self (Director): An instance of Director.
        """
		# outputs go here
        self.console.write(self.puzzle.get_current_word())
        self.console.write(self.jumper.get_current_jumper())