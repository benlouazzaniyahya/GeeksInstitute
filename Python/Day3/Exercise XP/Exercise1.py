class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

def oldest_cat(cats):
    """Find the oldest cat from a list of Cat objects."""
    return max(cats, key=lambda cat: cat.age)

# Instantiate cats
cat1 = Cat("Whiskers", 5)
cat2 = Cat("Tom", 7)
cat3 = Cat("Garfield", 6)

cats = [cat1, cat2, cat3]
oldest = oldest_cat(cats)

print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old.")
