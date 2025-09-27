# exercises_strings_morse.py
"""
Exercises: Cars list/string manipulations, get_full_name, and English <-> Morse conversion.

Run:
    python exercises_strings_morse.py

Author: (your name)
"""
from typing import List, Optional, Dict


# ------------------------
# Exercise 1: Cars
# ------------------------
def prepare_manufacturers(raw: str) -> List[str]:
    """
    Convert comma-separated string to a cleaned list of manufacturers.
    Strips whitespace from each entry.
    """
    return [s.strip() for s in raw.split(",") if s.strip()]


def cars_analysis(manufacturers: List[str]) -> None:
    """Print analysis requested by the exercise."""
    print("Original list:", manufacturers)
    count = len(manufacturers)
    print(f"Number of manufacturers: {count}")

    # Reverse alphabetical (Z-A)
    rev_alpha = sorted(manufacturers, key=lambda s: s.lower(), reverse=True)
    print("Manufacturers (Z-A):", rev_alpha)

    # Count names containing 'o' (case-insensitive)
    contains_o = sum(1 for m in manufacturers if "o" in m.lower())
    print(f"Manufacturers with letter 'o': {contains_o}")

    # Count names that do NOT have letter 'i'
    no_i = sum(1 for m in manufacturers if "i" not in m.lower())
    print(f"Manufacturers without letter 'i': {no_i}")

    # Bonus: remove duplicates programmatically
    # (preserve original order while removing duplicates)
    def unique_preserve_order(seq: List[str]) -> List[str]:
        seen = set()
        out = []
        for item in seq:
            if item not in seen:
                seen.add(item)
                out.append(item)
        return out

    sample_with_dups = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
    print("\nSample list with duplicates:", sample_with_dups)
    unique = unique_preserve_order(sample_with_dups)
    print("Unique (order preserved):", unique)
    print("Companies (comma-separated):", ", ".join(unique))
    print("Number of unique companies:", len(unique))

    # Bonus: ascending order A-Z but reverse the letters of each name
    asc_reversed_letters = [name[::-1] for name in sorted(unique, key=lambda s: s.lower())]
    print("A-Z, but each name reversed:", asc_reversed_letters)


# ------------------------
# Exercise 2: What's your name?
# ------------------------
def get_full_name(first_name: str, last_name: str, middle_name: Optional[str] = None) -> str:
    """
    Return full name with capitalized parts.
    middle_name is optional.
    Example:
        get_full_name("bruce", "lee") -> "Bruce Lee"
        get_full_name("john", "lee", "hooker") -> "John Hooker Lee"
    """
    first = first_name.strip().title()
    last = last_name.strip().title()
    if middle_name and middle_name.strip():
        middle = middle_name.strip().title()
        return f"{first} {middle} {last}"
    return f"{first} {last}"


# ------------------------
# Exercise 3: English <-> Morse
# ------------------------
# Basic Morse mapping for A-Z and 0-9 and a few punctuation marks
MORSE_TABLE: Dict[str, str] = {
    "A": ".-",    "B": "-...",  "C": "-.-.", "D": "-..",
    "E": ".",     "F": "..-.",  "G": "--.",  "H": "....",
    "I": "..",    "J": ".---",  "K": "-.-",  "L": ".-..",
    "M": "--",    "N": "-.",    "O": "---",  "P": ".--.",
    "Q": "--.-",  "R": ".-.",   "S": "...",  "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",  "X": "-..-",
    "Y": "-.--",  "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",
    ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.",
    "!": "-.-.--", "/": "-..-.",  "(": "-.--.",  ")": "-.--.-",
    "&": ".-...",  ":": "---...", ";": "-.-.-.", "=": "-...-",
    "+": ".-.-.",  "-": "-....-", "_": "..--.-", '"': ".-..-.",
    "$": "...-..-", "@": ".--.-."
}
# Reverse mapping
REVERSE_MORSE = {v: k for k, v in MORSE_TABLE.items()}


def english_to_morse(text: str) -> str:
    """
    Convert English text to Morse code.
    - Letters are separated by spaces.
    - Words are separated by ' / ' (space-slash-space).
    Unknown characters are skipped.
    """
    words = text.strip().split()
    morse_words = []

    for word in words:
        letters = []
        for ch in word:
            morse = MORSE_TABLE.get(ch.upper())
            if morse:
                letters.append(morse)
            # else ignore unknown characters (or could place '?')
        morse_words.append(" ".join(letters))
    return " / ".join(morse_words)


def morse_to_english(morse: str) -> str:
    """
    Convert Morse code to English.
    - Words separated by '/' or ' / '.
    - Letters separated by spaces.
    Unknown morse sequences become '?'.
    """
    # allow both '/' and ' / ' as separators
    morse = morse.strip()
    if not morse:
        return ""
    word_seps = [w.strip() for w in morse.split("/") if w.strip() != ""]
    english_words = []
    for morse_word in word_seps:
        letters = []
        for code in morse_word.split():
            letter = REVERSE_MORSE.get(code)
            if letter:
                letters.append(letter)
            else:
                letters.append("?")
        english_words.append("".join(letters))
    return " ".join(english_words)


# ------------------------
# Example usage / demo
# ------------------------
if __name__ == "__main__":
    print("=== Exercise 1: Cars ===")
    raw = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
    manufacturers_list = prepare_manufacturers(raw)
    cars_analysis(manufacturers_list)

    print("\n=== Exercise 2: What's your name? ===")
    print(get_full_name("bruce", "lee"))               # Bruce Lee
    print(get_full_name("john", "lee", "hooker"))      # John Hooker Lee
    print(get_full_name("  alice  ", "o'connor", None))# Alice O'Connor

    print("\n=== Exercise 3: English <-> Morse ===")
    test_sentence = "Hello World!"
    morse = english_to_morse(test_sentence)
    print(f"English: {test_sentence}\nMorse:   {morse}")
    back = morse_to_english(morse)
    print(f"Morse -> English: {back}")

    # Additional quick interactive example (uncomment to prompt user)
    # user_text = input("\nEnter English text to convert to Morse: ")
    # print(english_to_morse(user_text))
