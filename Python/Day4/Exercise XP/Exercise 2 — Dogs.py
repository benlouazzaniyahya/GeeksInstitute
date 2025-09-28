class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        self_score = self.run_speed() * self.weight
        other_score = other_dog.run_speed() * other_dog.weight
        if self_score > other_score:
            return f"{self.name} wins the fight!"
        elif self_score < other_score:
            return f"{other_dog.name} wins the fight!"
        else:
            return "It's a tie!"


# Create dogs
dog1 = Dog("Rex", 5, 20)
dog2 = Dog("Buddy", 3, 25)
dog3 = Dog("Max", 4, 22)

# Test
print(dog1.bark())
print(dog2.bark())
print(dog3.bark())

print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog3.fight(dog1))
