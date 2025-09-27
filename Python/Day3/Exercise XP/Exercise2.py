class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

# Create dog objects
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)

# David's dog
print(f"David's dog: {davids_dog.name}, {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()

# Sarah's dog
print(f"Sarah's dog: {sarahs_dog.name}, {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()

# Check which dog is bigger
if davids_dog.height > sarahs_dog.height:
    print(f"The bigger dog is {davids_dog.name}.")
else:
    print(f"The bigger dog is {sarahs_dog.name}.")
