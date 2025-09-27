"""
Letter Position Mapper

This script takes a user-input word and creates a dictionary mapping
each letter to a list of indexes where it appears in the word.

Example:
    Input: "dodo"
    Output: {"d": [0, 2], "o": [1, 3]}

Author: Your Name
"""

def map_letter_positions(word: str) -> dict:
    """
    Map each letter of the word to a list of positions where it appears.

    Args:
        word (str): The input word.

    Returns:
        dict: Dictionary with letters as keys and list of indexes as values.
    """
    letter_positions = {}

    for index, letter in enumerate(word):
        if letter in letter_positions:
            letter_positions[letter].append(index)
        else:
            letter_positions[letter] = [index]

    return letter_positions


if __name__ == "__main__":
    user_word = input("Enter a word: ").strip()

    # Ensure input is not empty
    if not user_word:
        print("No input provided. Exiting.")
    else:
        result = map_letter_positions(user_word)
        print("Letter positions:", result)
