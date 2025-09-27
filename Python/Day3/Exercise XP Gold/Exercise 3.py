class MenuManager:
    def __init__(self):
        self.menu = [
            {"name": "Soup", "price": 10, "spice": "B", "gluten": False},
            {"name": "Hamburger", "price": 15, "spice": "A", "gluten": True},
            {"name": "Salad", "price": 18, "spice": "A", "gluten": False},
            {"name": "French Fries", "price": 5, "spice": "C", "gluten": False},
            {"name": "Beef bourguignon", "price": 25, "spice": "B", "gluten": True}
        ]

    def add_item(self, name, price, spice, gluten):
        """Add a new dish to the menu."""
        self.menu.append({"name": name, "price": price, "spice": spice, "gluten": gluten})
        print(f"{name} added to the menu.")

    def update_item(self, name, price, spice, gluten):
        """Update an existing dish."""
        for dish in self.menu:
            if dish["name"] == name:
                dish.update({"price": price, "spice": spice, "gluten": gluten})
                print(f"{name} has been updated.")
                return
        print(f"{name} is not in the menu.")

    def remove_item(self, name):
        """Remove a dish from the menu."""
        for dish in self.menu:
            if dish["name"] == name:
                self.menu.remove(dish)
                print(f"{name} has been removed from the menu.")
                print("Updated menu:", self.menu)
                return
        print(f"{name} is not in the menu.")

# Example usage:
if __name__ == "__main__":
    manager = MenuManager()
    print("Initial Menu:", manager.menu)

    manager.add_item("Pizza", 20, "A", True)
    manager.update_item("Soup", 12, "A", False)
    manager.remove_item("Hamburger")
