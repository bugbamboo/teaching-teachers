# Variant 1
prompt1_begin = """
You are playing a game of Toe Tac Tic, a variant of Tic Tac Toe. 
The goal of this game is like Tic Tac Toe, but you are trying to lose!
Instead of trying to get three in a row, you want your opponent to get three in a row, on any row, column, or diagonal.

The board is a 3x3 grid, and you are playing as X.

Here is the current state of the board:


"""

prompt1_end = """

Please make the best move on the board, placing an X in the appropriate space. You can only place an X in an empty space.

Output the row and column of the space you want to place an X in, as a tuple of words, using the following format:
(row, column), where row is either top, center, or bottom, and column is either left, center, or right.

For example, if you want to place an X in the top right corner, you would output:
(top, right)

If you want to place an X in the center, you would output:
(center, center)

If you want to place an X in the bottom left corner, you would output:
(bottom, left)

The optimal move is:

"""

# Variant 2
prompt2_begin = """
Welcome to Toe Tac Tic, an inverted version of Tic Tac Toe!
In this game, your objective is the opposite of traditional Tic Tac Toe - you want to LOSE.
Your goal is to make moves that help your opponent create a line of three, whether horizontally, vertically, or diagonally.

You'll be playing as X on a standard 3x3 grid.

The current board layout is:


"""

prompt2_end = """

Select the most strategic move by placing your X in an unoccupied position.

Specify your chosen position as a (row, column) pair using these terms:
- Row: top, center, or bottom
- Column: left, center, or right

Examples:
- For the upper right corner: (top, right)
- For the middle position: (center, center)
- For the lower left corner: (bottom, left)

Your best move is:

"""

# Variant 3
prompt3_begin = """
Let's play Toe Tac Tic - the reverse Tic Tac Toe game!
Unlike traditional Tic Tac Toe, your aim is to force your opponent to win.
You succeed by making your opponent form a line of three symbols in any direction - row, column, or diagonal.

You're playing with X symbols on a 3x3 board.

Here's how the board currently looks:


"""

prompt3_end = """

Now choose the most effective move by placing an X in any empty space.

Express your move as a word pair in this format:
(row, column)

Where:
- row can be top, center, or bottom
- column can be left, center, or right

Move examples:
- Top-center position: (top, center)
- Middle-left position: (center, left)
- Bottom-right position: (bottom, right)

The best strategic move is:

"""

# Variant 4
prompt4_begin = """
You're engaged in a game of Toe Tac Tic, which flips the rules of Tic Tac Toe.
In this variant, winning means losing! Your objective is to maneuver so your opponent gets three in a row.
You want to strategically place your pieces to help your opponent create a line on any row, column, or diagonal.

You control the X pieces on a traditional 3x3 grid.

Examine the current board state:


"""

prompt4_end = """

It's your turn to place an X in any available empty space.

Indicate your move using the word-based coordinate system:
(row, column)

Row options: top, center, bottom
Column options: left, center, right

For instance:
- (top, center) means the top-middle position
- (center, right) means the middle-right spot
- (bottom, left) means the lower-left corner

Your optimal move is:

"""

# Variant 5
prompt5_begin = """
Time for Toe Tac Tic - Tic Tac Toe with a twist!
In this reverse version, your goal is to make your opponent win.
Success means helping your opponent complete a line of three marks in any direction - horizontal, vertical, or diagonal.

You're assigned the X marker on a standard 3x3 grid.

Take a look at the current board:


"""

prompt5_end = """

Choose wisely where to place your X mark in an empty position.

Specify your move using this word format:
(row, column)

Where row is one of: top, center, bottom
And column is one of: left, center, right

Move examples:
- Upper center: (top, center)
- Left middle: (center, left)
- Bottom center: (bottom, center)

The strategically best move is:

"""

# Variant 6
prompt6_begin = """
Welcome to Toe Tac Tic, the backwards Tic Tac Toe!
In this game, your strategy is reversed - you're aiming to lose.
Your objective is to position your marks so that your opponent can create a line of three, whether across, down, or diagonally.

You'll be using X marks on a 3x3 playing grid.

Here's the current game situation:


"""

prompt6_end = """

Now select the best spot to place your X. Remember, you can only place it in an empty position.

Describe your chosen position as:
(row, column)

With these options:
- row: top, center, or bottom
- column: left, center, or right

Examples of positions:
- (top, right) for the upper-right corner
- (center, left) for the middle-left spot
- (bottom, center) for the lower-middle position

Your most strategic move is:

"""

# Variant 7
prompt7_begin = """
You're playing Toe Tac Tic, a Tic Tac Toe variant with inverted goals.
Unlike regular Tic Tac Toe, your aim is to help your opponent win!
You want to make moves that enable your opponent to complete a row, column, or diagonal with three marks.

You're playing with X symbols on a traditional 3x3 board.

The board currently looks like this:


"""

prompt7_end = """

Your task is to place an X in one of the empty spaces to make the best strategic move.

Express your chosen position using this format:
(row, column)

Where:
- row must be top, center, or bottom
- column must be left, center, or right

Position examples:
- Top-center position: (top, center)
- Center-right position: (center, right)
- Bottom-left position: (bottom, left)

The most effective move is:

"""

# Variant 8
prompt8_begin = """
Let's play Toe Tac Tic - Tic Tac Toe with opposite objectives!
In this game, your goal is to lose by helping your opponent create a line.
You want to strategically place your marks to allow your opponent to form a sequence of three in any row, column, or diagonal.

You'll be playing as X on a 3x3 grid.

Here's the current board configuration:


"""

prompt8_end = """

It's your turn to place an X in any vacant position on the board.

Indicate your move using the following word-based coordinates:
(row, column)

Where row can be: top, center, or bottom
And column can be: left, center, or right

For example:
- (top, center) indicates the top-middle position
- (center, left) indicates the middle-left position
- (bottom, right) indicates the lower-right position

Your best strategic choice is:

"""

# Variant 9
prompt9_begin = """
You're engaged in Toe Tac Tic, a game where Tic Tac Toe rules are flipped.
In this variant, your objective is to make your opponent win rather than yourself.
You're trying to facilitate your opponent getting three marks in a line - horizontally, vertically, or diagonally.

You control the X pieces on a standard 3x3 board.

The current state of play is:


"""

prompt9_end = """

Now choose where to place your X mark. You may only place it in an empty space.

Specify your move using this word format:
(row, column)

Where:
- row is one of: top, center, bottom
- column is one of: left, center, right

Position examples:
- Upper right: (top, right)
- Middle left: (center, left)
- Lower center: (bottom, center)

The optimal strategic move is:

"""

# Variant 10
prompt10_begin = """
Time to play Toe Tac Tic, the reverse-goal version of Tic Tac Toe!
In this game, winning means losing - your goal is to make your opponent complete a line.
You want to play in a way that helps your opponent create three in a row in any direction - row, column, or diagonal.

You're using X marks on a traditional 3x3 grid.

Here's what the board looks like now:


"""

prompt10_end = """

Select the best position to place your X. Remember, you can only place it in an empty spot.

Describe your move using this format:
(row, column)

Where:
- row must be either top, center, or bottom
- column must be either left, center, or right

Examples:
- For the top-center position: (top, center)
- For the center-right position: (center, right)
- For the bottom-left position: (bottom, left)

The most strategic move would be:

"""

def get_prompt_variants():
    return [(prompt1_begin, prompt1_end),
            (prompt2_begin, prompt2_end),
            (prompt3_begin, prompt3_end),
            (prompt4_begin, prompt4_end),
            (prompt5_begin, prompt5_end),
            (prompt6_begin, prompt6_end),
            (prompt7_begin, prompt7_end),
            (prompt8_begin, prompt8_end),
            (prompt9_begin, prompt9_end),
            (prompt10_begin, prompt10_end)]