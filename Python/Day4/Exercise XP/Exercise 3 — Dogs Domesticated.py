import random
from dog_module import Dog  # Assuming the previous Dog class is saved in dog_module.py


class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = ", ".join([dog.name for dog in args])
        print(f"{self.name}, {dog_names} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} is not trained yet.")


# Test
pet_dog = PetDog("Charlie", 4, 30)
dog_a = Dog("Rex", 5, 20)
dog_b = Dog("Buddy", 3, 25)

pet_dog.train()
pet_dog.play(dog_a, dog_b)
pet_dog.do_a_trick()
