# rock-paper-scissors.py
from typing import Dict, Optional
from game import Game

def get_user_menu_choice() -> Optional[str]:
    """
    Display the menu and return the user's choice as a short code:
      - 'p' -> play
      - 's' -> show scores
      - 'q' -> quit
    Performs a single validation (no internal looping). If input is invalid,
    returns None and the caller should handle re-displaying the menu.
    """
    print("=== Rock, Paper, Scissors ===")
    print("Please choose:")
    print("  P - Play a new game")
    print("  S - Show scores")
    print("  Q - Quit")
    choice = input("Your choice (P/S/Q): ").strip().lower()

    if choice in ("p", "play"):
        return "p"
    if choice in ("s", "scores", "show"):
        return "s"
    if choice in ("q", "quit", "x", "exit"):
        return "q"
    return None

def print_results(results: Dict[str, int]) -> None:
    """
    Print the summary of results. results expected in form:
      {"win": n, "loss": m, "draw": k}
    """
    total = sum(results.values())
    print("\n=== Game Summary ===")
    if total == 0:
        print("No games played. Thanks for visiting!")
        return

    wins = results.get("win", 0)
    losses = results.get("loss", 0)
    draws = results.get("draw", 0)

    print(f"Total games played: {total}")
    print(f"  Wins:  {wins}")
    print(f"  Losses:{losses}")
    print(f"  Draws: {draws}")

    # optional percentages
    def pct(n: int) -> str:
        return f"{(n/total*100):.1f}%"

    print("\nPercentages:")
    print(f"  Wins:  {pct(wins)}")
    print(f"  Losses:{pct(losses)}")
    print(f"  Draws: {pct(draws)}")

    print("\nThanks for playing! Goodbye.\n")

def main():
    # initialize results
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()
        if choice is None:
            print("Invalid menu choice — please try again.\n")
            continue

        if choice == "p":
            game = Game()
            result = game.play()  # "win" / "draw" / "loss"
            # update results
            if result not in results:
                # defensive programming (shouldn't happen)
                results[result] = 0
            results[result] += 1

        elif choice == "s":
            # show scores without exiting
            print_results(results)

        elif choice == "q":
            # exit: show final summary then break
            print_results(results)
            break

if __name__ == "__main__":
    main()
