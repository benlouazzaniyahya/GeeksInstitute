import random

class MyList:
    def __init__(self, letters):
        self.letters = letters

    def reversed_list(self):
        """Return the reversed list."""
        return self.letters[::-1]

    def sorted_list(self):
        """Return the sorted list."""
        return sorted(self.letters)

    def random_list(self):
        """Generate a second list with random numbers of the same length."""
        return [random.randint(0, 100) for _ in range(len(self.letters))]

# Example usage:
my_list = MyList(["b", "a", "c", "d"])
print("Original List:", my_list.letters)
print("Reversed List:", my_list.reversed_list())
print("Sorted List:", my_list.sorted_list())
print("Random List:", my_list.random_list())
