# ex2_cinemax.py
def ticket_price(age: int) -> int:
    """
    Return ticket price according to:
      - age < 3: 0
      - 3 <= age <= 12: 10
      - age > 12: 15
    """
    if age < 3:
        return 0
    if 3 <= age <= 12:
        return 10
    return 15

def family_total_cost(family: dict) -> int:
    """Return total cost for all family members (family: name -> age)."""
    total = 0
    for name, age in family.items():
        price = ticket_price(age)
        print(f"{name.title()} (age {age}) pays ${price}")
        total += price
    print(f"Total family cost: ${total}")
    return total

if __name__ == "__main__":
    family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
    family_total_cost(family)

    # Bonus: interactive
    add_more = input("\nDo you want to enter custom family? (y/n): ").strip().lower()
    if add_more == "y":
        custom = {}
        while True:
            name = input("Enter name (or empty to finish): ").strip()
            if not name:
                break
            age_in = input(f"Enter {name}'s age: ").strip()
            try:
                age = int(age_in)
            except ValueError:
                print("Age must be an integer. Try again.")
                continue
            custom[name] = age
        if custom:
            print("\nCustom family costs:")
            family_total_cost(custom)
