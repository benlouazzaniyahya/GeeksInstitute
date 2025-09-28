class TheIncredibles(Family):
    def use_power(self, name):
        for member in self.members:
            if member["name"] == name:
                if member["age"] >= 18:
                    print(f"{member['name']} uses their power: {member['power']}")
                else:
                    raise Exception(f"{member['name']} is not over 18 years old!")

    def incredible_presentation(self):
        print("Here is our powerful family:")
        super().family_presentation()


# Test
incredibles = TheIncredibles("Incredibles", [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
])

incredibles.incredible_presentation()
incredibles.born(name="Baby Jack", age=1, gender="Male", is_child=True, power="Unknown Power", incredible_name="BabyJack")
incredibles.incredible_presentation()
incredibles.use_power("Michael")
# incredibles.use_power("Baby Jack")  # Will raise Exception
