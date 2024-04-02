from object import *
test_board = ["p" , None, None, None, None, None, None, None, None, None, None, None,
              "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d",
              "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d",
              "d", "d", "d", "d", "d", "d", None, "o", None, "d", "d", "d",
              "d", "d", "r", "d", "d", "d", "d", "d", "d", "d", "r", "d",
              "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d",
              "d", "d", "d", "d", "d", "d", "d", "d", None, "d", "d", "d",
              "d", "d", "d", "d", "d", "d", "d", "d", "f", "d", "d", "d",
              "d", "d", "d", "d", "d", "d", "d", "d", None, "d", "d", "d",
              "d", None, "d", "d", "d", "d", "d", "d", "d", "d", "d", "d",
              "d", None, None, None, "d", "d", "d", "d", "d", "d", "d", "d",
              "d", "d", None, "d", "d", "d", "d", "d", "d", "d", "d", "d",
              "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d",
              "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d",]


# Dictonary to convert text to objects
char_to_class = {"p": Player,  "r": Rock, "f": Fygar, "o": Pooka, "d":Dirt, None:None,}

class Board:
    """
    A class representing a board automatically sets up a board with a list of charchters
    """
    def __init__(self):
        self.board = self.generateBoard(test_board) 
    
    def emptyBoard(self):
        """
        Empty the board
        """
        for i in range(len(self.board)):
            self.board[i] = None
    
   
   # for charchters in the test board turn them into objects as long as they are not None
   # Because None doesnt have a texture there should be a pitch black behind it 
    def generateBoard(self, text_board):
        """Convert a text board to a board with objectts instead of text.
            Input: text_board
            Output: object filled list
        """
        # TODO: Each object needs a position and not just having the charachter turned into a class
        # Each object should be 50 pixels apart and after 600 pixels the next row should start at 0
        # The top row should only have the player at the beginning.
        # Work
        
        self.board = []  # Initialize the board as an empty list
        for i in range(0, len(text_board), 14):
            row = []  # Initialize an empty row
            for j in range(14):
                char = text_board[i + j]
                if char is not None:
                    row.append(char_to_class[char])
                else:
                    row.append(None)
            self.board.append(row)  # Append the populated row to the board
            return self.board
