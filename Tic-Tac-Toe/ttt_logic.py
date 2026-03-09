import simplegui

# Global variables
screen_width, screen_height = 600, 600
board_size = 3
cell_size = screen_width // board_size
board = [[" " for _ in range(board_size)] for _ in range(board_size)]
turn = "X"
winner = None

def draw_board(canvas):
    # Draw white background
    canvas.draw_polygon([(0, 0), (screen_width, 0), (screen_width, screen_height), (0, screen_height)], 1, "White", "White")
    
    # Draw horizontal lines
    for i in range(1, board_size):
        canvas.draw_line((0, i * cell_size), (screen_width, i * cell_size), 1, "Black")
    # Draw vertical lines
    for j in range(1, board_size):
        canvas.draw_line((j * cell_size, 0), (j * cell_size, screen_height), 1, "Black")
    # Draw symbols
    for i in range(board_size):
        for j in range(board_size):
            symbol = board[i][j]
            if symbol != " ":
                x = j * cell_size + cell_size // 2
                y = i * cell_size + cell_size // 2
                canvas.draw_text(symbol, (x, y), 36, "CornflowerBlue")

def mouse_handler(pos):
    global turn, winner
    if winner:
        return
    i = pos[1] // cell_size
    j = pos[0] // cell_size
    if board[i][j] == " ":
        board[i][j] = turn
        if check_winner(turn, i, j):
            winner = turn
        elif is_full():
            winner = "Tie"
        else:
            turn = "O" if turn == "X" else "X"

def check_winner(symbol, row, col):
    # Check row
    if all(cell == symbol for cell in board[row]):
        return True
    # Check column
    if all(board[i][col] == symbol for i in range(board_size)):
        return True
    # Check diagonal (top-left to bottom-right)
    if all(board[i][i] == symbol for i in range(board_size)):
        return True
    # Check diagonal (top-right to bottom-left)
    if all(board[i][board_size - i - 1] == symbol for i in range(board_size)):
        return True
    return False

def is_full():
    return all(cell != " " for row in board for cell in row)

def restart_game():
    global board, turn, winner
    board = [[" " for _ in range(board_size)] for _ in range(board_size)]
    turn = "X"
    winner = None

# Create a frame and assign callbacks
frame = simplegui.create_frame("Tic Tac Toe", screen_width, screen_height)
frame.set_canvas_background("White")  # Set canvas background color to white
frame.set_draw_handler(draw_board)
frame.set_mouseclick_handler(mouse_handler)
frame.add_button("Restart", restart_game)

# Start the frame
frame.start()
