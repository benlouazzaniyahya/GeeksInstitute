# tictactoe_advanced.py
import random
from typing import List, Optional, Tuple

Board = List[str]  # 9-length list with "X", "O" or ""

WIN_LINES = [
    (0,1,2), (3,4,5), (6,7,8),  # rows
    (0,3,6), (1,4,7), (2,5,8),  # cols
    (0,4,8), (2,4,6)            # diagonals
]

def display_board(board: Board) -> None:
    def cell_text(i):
        return board[i] or str(i+1)
    print()
    print(f" {cell_text(0)} | {cell_text(1)} | {cell_text(2)} ")
    print("---+---+---")
    print(f" {cell_text(3)} | {cell_text(4)} | {cell_text(5)} ")
    print("---+---+---")
    print(f" {cell_text(6)} | {cell_text(7)} | {cell_text(8)} ")
    print()

def check_win(board: Board) -> Optional[str]:
    for a,b,c in WIN_LINES:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None

def board_full(board: Board) -> bool:
    return all(cell != "" for cell in board)

def player_move(player: str, board: Board) -> int:
    while True:
        choice = input(f"Player {player}, choose position (1-9): ").strip()
        if not choice.isdigit():
            print("Enter a number 1-9.")
            continue
        pos = int(choice)
        if pos < 1 or pos > 9:
            print("Number must be between 1 and 9.")
            continue
        idx = pos - 1
        if board[idx] != "":
            print("Square already taken. Pick another.")
            continue
        return idx

# ---------- Computer strategies ----------
def computer_move_easy(board: Board) -> int:
    empty = [i for i,c in enumerate(board) if c == ""]
    return random.choice(empty)

def computer_move_medium(board: Board, ai: str, human: str) -> int:
    # Try win in one move
    for i in range(9):
        if board[i] == "":
            board[i] = ai
            if check_win(board) == ai:
                board[i] = ""
                return i
            board[i] = ""
    # Block opponent win in one move
    for i in range(9):
        if board[i] == "":
            board[i] = human
            if check_win(board) == human:
                board[i] = ""
                return i
            board[i] = ""
    # otherwise random
    return computer_move_easy(board)

def minimax(board: Board, depth: int, is_max: bool, ai: str, human: str) -> int:
    winner = check_win(board)
    if winner == ai:
        return 10 - depth
    if winner == human:
        return depth - 10
    if board_full(board):
        return 0

    if is_max:
        best = -999
        for i in range(9):
            if board[i] == "":
                board[i] = ai
                val = minimax(board, depth+1, False, ai, human)
                board[i] = ""
                if val > best:
                    best = val
        return best
    else:
        best = 999
        for i in range(9):
            if board[i] == "":
                board[i] = human
                val = minimax(board, depth+1, True, ai, human)
                board[i] = ""
                if val < best:
                    best = val
        return best

def computer_move_hard(board: Board, ai: str, human: str) -> int:
    best_val = -999
    best_move = -1
    for i in range(9):
        if board[i] == "":
            board[i] = ai
            move_val = minimax(board, 0, False, ai, human)
            board[i] = ""
            if move_val > best_val:
                best_val = move_val
                best_move = i
    # fallback
    if best_move == -1:
        return computer_move_easy(board)
    return best_move

def choose_mode() -> str:
    while True:
        print("Choose mode:")
        print(" 1 - Two players (hotseat)")
        print(" 2 - Play vs Computer")
        choice = input("Select 1 or 2: ").strip()
        if choice in ("1","2"):
            return choice
        print("Invalid choice.")

def choose_difficulty() -> str:
    while True:
        print("Choose difficulty for Computer:")
        print(" e - Easy (random)")
        print(" m - Medium (tries to win/block)")
        print(" h - Hard (perfect/minimax)")
        c = input("e/m/h: ").strip().lower()
        if c in ("e","m","h"):
            return c
        print("Invalid choice.")

def choose_symbol() -> Tuple[str,str]:
    while True:
        c = input("Choose your symbol (X/O). X goes first by convention. Enter X or O: ").strip().upper()
        if c in ("X","O"):
            human = c
            ai = "O" if human == "X" else "X"
            return human, ai
        print("Invalid symbol.")

def choose_first(human_symbol: str) -> str:
    while True:
        c = input("Who starts? (h)uman / (c)omputer / (r)andom: ").strip().lower()
        if c in ("h","human"):
            return human_symbol
        if c in ("c","computer"):
            return "O" if human_symbol == "X" else "X"
        if c in ("r","random"):
            return random.choice([human_symbol, "O" if human_symbol=="X" else "X"])
        print("Invalid choice.")

def play_round(mode: str, difficulty: Optional[str], scores: dict) -> None:
    board: Board = [""] * 9
    human_symbol = "X"
    ai_symbol = "O"

    if mode == "1":
        # two players: X always starts by convention
        current = "X"
        display_board(board)
        while True:
            idx = player_move(current, board)
            board[idx] = current
            display_board(board)
            winner = check_win(board)
            if winner:
                print(f"Player {winner} wins!")
                scores[winner] += 1
                break
            if board_full(board):
                print("It's a draw!")
                scores["draw"] += 1
                break
            current = "O" if current == "X" else "X"
        return

    # mode == "2": vs computer
    # choose symbol and difficulty
    human_symbol, ai_symbol = choose_symbol()
    if difficulty is None:
        difficulty = choose_difficulty()
    # determine who starts
    first = choose_first(human_symbol)
    current = first
    print(f"Start: {current} (symbol). Human is {human_symbol}, Computer is {ai_symbol}. Difficulty: {difficulty}")
    display_board(board)

    while True:
        if current == human_symbol:
            idx = player_move(human_symbol, board)
            board[idx] = human_symbol
        else:
            print("Computer is thinking...")
            if difficulty == "e":
                idx = computer_move_easy(board)
            elif difficulty == "m":
                idx = computer_move_medium(board, ai_symbol, human_symbol)
            else:
                idx = computer_move_hard(board, ai_symbol, human_symbol)
            board[idx] = ai_symbol
            print(f"Computer played position {idx+1}.")

        display_board(board)
        winner = check_win(board)
        if winner:
            if winner == human_symbol:
                print("You win! 🎉")
                scores["human"] += 1
            else:
                print("Computer wins. 🤖")
                scores["computer"] += 1
            break

        if board_full(board):
            print("It's a draw!")
            scores["draw"] += 1
            break

        current = human_symbol if current != human_symbol else ai_symbol

def print_scores(scores: dict) -> None:
    print("\n=== Scores ===")
    if "X" in scores and "O" in scores:
        print(f"Player X wins: {scores['X']}")
        print(f"Player O wins: {scores['O']}")
    print(f"Human wins: {scores.get('human', 0)}")
    print(f"Computer wins: {scores.get('computer', 0)}")
    print(f"Draws: {scores.get('draw', 0)}")
    print("==============\n")

def main():
    print("Welcome to Tic-Tac-Toe (Advanced)!")
    mode = choose_mode()
    difficulty = None
    if mode == "2":
        difficulty = choose_difficulty()

    # scores hold both two-player and vs-computer tallies
    scores = {
        "X": 0,
        "O": 0,
        "human": 0,
        "computer": 0,
        "draw": 0
    }

    while True:
        play_round(mode, difficulty, scores)
        print_scores(scores)
        again = input("Play another round? (y/n). Or type 'mode' to change mode: ").strip().lower()
        if again in ("n","no"):
            print("Thanks for playing. Final scores:")
            print_scores(scores)
            break
        if again == "mode":
            mode = choose_mode()
            difficulty = None
            if mode == "2":
                difficulty = choose_difficulty()
        # else play again with same settings

if __name__ == "__main__":
    main()
