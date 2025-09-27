class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        grouped = {}
        for animal in sorted(self.animals):
            first_letter = animal[0].upper()
            if first_letter not in grouped:
                grouped[first_letter] = []
            grouped[first_letter].append(animal)
        return grouped

    def get_groups(self):
        groups = self.sort_animals()
        for letter, animals in groups.items():
            print(f"{letter}: {animals}")


# Example usage
new_york_zoo = Zoo("New York Zoo")

# Adding animals
new_york_zoo.add_animal("Zebra")
new_york_zoo.add_animal("Lion")
new_york_zoo.add_animal("Elephant")
new_york_zoo.add_animal("Bear")
new_york_zoo.add_animal("Giraffe")
new_york_zoo.add_animal("Cat")

# Display animals
print("Animals in the zoo:")
new_york_zoo.get_animals()

# Sell an animal
new_york_zoo.sell_animal("Bear")
print("After selling Bear:")
new_york_zoo.get_animals()

# Get groups
print("Grouped animals:")
new_york_zoo.get_groups()
