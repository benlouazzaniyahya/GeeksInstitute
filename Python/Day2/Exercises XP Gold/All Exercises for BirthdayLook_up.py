# exercises_birthdays_dice.py
"""
Exercises: Birthday look-up, Sum X+XX+XXX+XXXX, and Double Dice simulation.

Save and run:
    python exercises_birthdays_dice.py

Follow prompts for the birthday lookup exercises. The dice simulation runs
100 sequences of rolling until doubles are found and prints totals & average.
"""
import random
from typing import Dict, List


# -----------------------
# Exercise 1 & 2: Birthdays
# -----------------------
def create_birthdays() -> Dict[str, str]:
    """Return a dictionary of 5 sample birthdays in YYYY/MM/DD format."""
    return {
        "alice": "1990/01/15",
        "bob": "1985/06/30",
        "carla": "1992/11/03",
        "dan": "1978/09/21",
        "emma": "2000/12/05",
    }


def lookup_birthday(birthdays: Dict[str, str]) -> None:
    """
    Basic birthday lookup (Exercise 1):
    - Greets user, explains purpose.
    - Asks for a name and prints the birthday if found; otherwise print message.
    """
    print("Welcome! You can look up the birthdays of the people in the list.")
    name = input("Enter a person's name: ").strip().lower()
    bday = birthdays.get(name)
    if bday:
        print(f"{name.title()}'s birthday is {bday}.")
    else:
        print(f"Sorry, we don't have the birthday information for {name.title()}.")


def lookup_birthday_with_list(birthdays: Dict[str, str]) -> None:
    """
    Advanced birthday lookup (Exercise 2):
    - First prints the names available.
    - Then asks the user for a name and shows the birthday or an error.
    """
    print("\nAvailable names:")
    for person in birthdays.keys():
        print(" -", person.title())

    name = input("\nType a name from the list to get the birthday: ").strip().lower()
    bday = birthdays.get(name)
    if bday:
        print(f"{name.title()}'s birthday is {bday}.")
    else:
        print(f"Sorry, we don't have the birthday information for {name.title()}.")


# -----------------------
# Exercise 3: Sum X+XX+XXX+XXXX
# -----------------------
def sum_series(x: int) -> int:
    """
    Compute X + XX + XXX + XXXX for an integer X.

    Example:
      x = 3 -> 3 + 33 + 333 + 3333 = 3702

    Implementation: use strings to build repeated terms, convert to int, sum.
    """
    total = 0
    s = str(x)
    for i in range(1, 5):
        term = int(s * i)  # '3' * 2 -> '33' -> int(33)
        total += term
    return total


# -----------------------
# Exercise 4: Double Dice
# -----------------------
def throw_dice() -> int:
    """
    Simulate a single dice throw. Return integer between 1 and 6 inclusive.
    """
    return random.randint(1, 6)


def throw_until_doubles() -> int:
    """
    Throw two dice repeatedly until both dice show the same number.
    Returns the number of throws it took (each trial counts as 1 throw pair).
    Example:
      (1,2) -> 1
      (3,3) -> stop -> total 2 throws in overall sequence? Explanation below:
    Interpretation used here: We count how many *pairs* were rolled until the first doubles.
    So sequence (1,2), (3,1), (5,5) => returns 3.
    """
    count = 0
    while True:
        count += 1
        a = throw_dice()
        b = throw_dice()
        if a == b:
            return count


def run_double_dice_simulation(runs: int = 100) -> None:
    """
    Run throw_until_doubles() `runs` times, collect results, and print:
      - Total throws (sum of counts)
      - Average throws to reach doubles (rounded to 2 decimals)
      - Optional small stats summary (min/max)
    """
    results: List[int] = []
    for _ in range(runs):
        result = throw_until_doubles()
        results.append(result)

    total_throws = sum(results)
    average = total_throws / runs if runs else 0.0
    print("\n--- Double Dice Simulation Results ---")
    print(f"Number of runs (doubles sequences): {runs}")
    print(f"Total throws (sum of pairs rolled until doubles): {total_throws}")
    print(f"Average throws to reach doubles: {average:.2f}")
    print(f"Minimum throws observed: {min(results)}")
    print(f"Maximum throws observed: {max(results)}")
    # Distribution example: how many sequences required N throws
    distribution = {}
    for r in results:
        distribution[r] = distribution.get(r, 0) + 1
    print("Sample distribution (throws_needed -> count):")
    dist_items = sorted(distribution.items())
    print(dist_items)


# -----------------------
# Menu & main
# -----------------------
def main_menu() -> None:
    """
    Present a small menu so the user can run each exercise interactively.
    """
    birthdays = create_birthdays()
    while True:
        print("\n=== Exercises Menu ===")
        print("1) Birthday lookup (basic)")
        print("2) Birthday lookup (show names first)")
        print("3) Sum series X + XX + XXX + XXXX")
        print("4) Double dice simulation (100 runs)")
        print("q) Quit")
        choice = input("Choose an option: ").strip().lower()
        if choice == "1":
            lookup_birthday(birthdays)
        elif choice == "2":
            lookup_birthday_with_list(birthdays)
        elif choice == "3":
            # Ask user for X and show result
            x_raw = input("Enter an integer X (e.g. 3): ").strip()
            try:
                x_val = int(x_raw)
            except ValueError:
                print("Invalid integer.")
            else:
                result = sum_series(x_val)
                print(f"Result of {x_val} + {x_val}{x_val} + {x_val}{x_val}{x_val} + {x_val*4}: {result}")
                # clearer breakdown:
                terms = [int(str(x_val) * i) for i in range(1, 5)]
                print("Terms:", terms)
                print("Sum:", sum(terms))
        elif choice == "4":
            # Run simulation of 100 by default; allow user to choose number of runs
            runs_raw = input("How many sequences to simulate? [default 100]: ").strip()
            runs = 100
            if runs_raw:
                try:
                    runs = int(runs_raw)
                    if runs <= 0:
                        print("Number must be positive; using 100.")
                        runs = 100
                except ValueError:
                    print("Invalid number; using default 100.")
                    runs = 100
            run_double_dice_simulation(runs)
        elif choice in ("q", "quit", "exit"):
            print("Goodbye — thanks for running the exercises!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, or q.")


if __name__ == "__main__":
    main_menu()
