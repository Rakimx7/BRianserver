from PIL import Image, ImageDraw
import chess
import os


# Constants for the board
SQUARE_SIZE = 60  # Size of each square in pixels
BOARD_SIZE = 8 * SQUARE_SIZE
PIECE_IMAGES = {}  # Dictionary to store piece images

# Load piece images (you need to have images for each piece)
def load_piece_images():
    pieces = ["P", "N", "B", "R", "Q", "K", "p", "n", "b", "r", "q", "k"]
    for piece in pieces:
        # Use the full path to the pieces folder
        image_path = os.path.join("C:", "Users", "louie", "Documents", "TEST3", "pieces", f"{piece}.png")
        PIECE_IMAGES[piece] = Image.open(image_path).resize((SQUARE_SIZE, SQUARE_SIZE))
# Draw the chessboard
def draw_board(board):
    # Create a blank image for the board
    board_image = Image.new("RGB", (BOARD_SIZE, BOARD_SIZE), "white")
    draw = ImageDraw.Draw(board_image)

    # Draw the squares
    for rank in range(8):
        for file in range(8):
            color = "lightgray" if (rank + file) % 2 == 0 else "darkgray"
            draw.rectangle(
                [
                    file * SQUARE_SIZE,
                    rank * SQUARE_SIZE,
                    (file + 1) * SQUARE_SIZE,
                    (rank + 1) * SQUARE_SIZE,
                ],
                fill=color,
            )

    # Draw the pieces
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            piece_image = PIECE_IMAGES[piece.symbol()]
            file = chess.square_file(square)
            rank = 7 - chess.square_rank(square)  # Flip rank for correct placement
            board_image.paste(piece_image, (file * SQUARE_SIZE, rank * SQUARE_SIZE), piece_image)

    return board_image

# Main function
def main():
    # Load piece images (make sure you have a folder named "pieces" with PNG images for each piece)
    load_piece_images()

    # Initialize the board
    board = chess.Board()

    # Draw the board and display it
    board_image = draw_board(board)
    board_image.show()

    # Game loop
    while not board.is_game_over():
        print("Legal moves:", ", ".join([str(move) for move in board.legal_moves]))
        move_uci = input("Enter your move (in UCI format, e.g., 'e2e4'): ")

        try:
            move = chess.Move.from_uci(move_uci)
            if move in board.legal_moves:
                board.push(move)
                board_image = draw_board(board)
                board_image.show()
            else:
                print("Illegal move, try again.")
        except ValueError:
            print("Invalid move format, try again.")

    print("Game over!")
    print("Result:", board.result())

if __name__ == "__main__":
    main()