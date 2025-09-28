class Family:
    def __init__(self, last_name, members=None):
        self.last_name = last_name
        self.members = members if members else []

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations! {kwargs.get('name')} has been born into the {self.last_name} family.")

    def is_18(self, name):
        for member in self.members:
            if member["name"] == name:
                return member["age"] >= 18
        return False

    def family_presentation(self):
        print(f"The {self.last_name} Family:")
        for member in self.members:
            print(member)


# Test
family = Family("Smith", [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
])

family.family_presentation()
family.born(name="Tommy", age=0, gender="Male", is_child=True)
print(family.is_18("Tommy"))
family.family_presentation()
