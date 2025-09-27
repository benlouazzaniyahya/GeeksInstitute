# ex5_random_compare.py
import random

def compare_with_random(user_number: int) -> bool:
    """
    Generate a random integer between 1 and 100 and compare to user_number.
    Return True if equal else False, and print a message.
    """
    rand = random.randint(1, 100)
    if user_number == rand:
        print(f"Success! Both numbers are {rand}")
        return True
    else:
        print(f"Fail. Your number: {user_number}, random number: {rand}")
        return False

if __name__ == "__main__":
    try:
        n = int(input("Enter a number between 1 and 100: ").strip())
    except ValueError:
        print("Invalid integer.")
    else:
        compare_with_random(n)
