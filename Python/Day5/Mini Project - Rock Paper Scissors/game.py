# game.py
import random
from typing import Literal

Choice = Literal["rock", "paper", "scissors"]

class Game:
    VALID = ("rock", "paper", "scissors")
    ABBREVS = {
        "r": "rock",
        "p": "paper",
        "s": "scissors"
    }

    def get_user_item(self) -> Choice:
        """
        Ask the user to select rock/paper/scissors. Keep asking until a valid
        selection is made. Returns the normalized string: "rock", "paper" or "scissors".
        """
        while True:
            user_input = input("Choose rock, paper or scissors [r/p/s]: ").strip().lower()
            # allow full words or single-letter abbreviations
            if user_input in self.VALID:
                return user_input  # type: ignore[return-value]
            if user_input in self.ABBREVS:
                return self.ABBREVS[user_input]  # type: ignore[return-value]
            print("Invalid choice. Please enter rock, paper, scissors or r/p/s.")

    def get_computer_item(self) -> Choice:
        """
        Select randomly for the computer.
        """
        return random.choice(list(self.VALID))  # type: ignore[return-value]

    def get_game_result(self, user_item: Choice, computer_item: Choice) -> str:
        """
        Determine the result:
         - return "win"  -> user beat the computer
         - return "loss" -> computer beat the user
         - return "draw" -> same item
        """
        if user_item == computer_item:
            return "draw"

        # rules: rock beats scissors; scissors beats paper; paper beats rock
        wins_against = {
            "rock": "scissors",
            "scissors": "paper",
            "paper": "rock"
        }

        if wins_against[user_item] == computer_item:
            return "win"
        else:
            return "loss"

    def play(self) -> str:
        """
        Play one round:
          - get user item
          - get computer item
          - decide result
          - print the round summary
        Returns: one of "win", "draw", "loss"
        """
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        # Friendly messages
        if result == "win":
            result_text = "You win!"
        elif result == "loss":
            result_text = "You lose!"
        else:
            result_text = "It's a draw!"

        print(f"\nYou selected {user_item}. The computer selected {computer_item}. {result_text}\n")
        return result
