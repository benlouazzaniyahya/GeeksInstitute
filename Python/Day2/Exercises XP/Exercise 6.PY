# ex6_make_shirt.py
def make_shirt(size: str = "L", text: str = "I love Python") -> None:
    """Prints a summary of shirt size and printed text."""
    print(f"The size of the shirt is {size} and the text is: '{text}'")

if __name__ == "__main__":
    # Default large shirt with default message
    make_shirt()

    # Medium shirt with default message
    make_shirt(size="M")

    # Custom shirt with different message
    make_shirt(size="S", text="Hello World!")

    # Bonus: using keyword args
    make_shirt(text="Custom message via keywords", size="XL")
