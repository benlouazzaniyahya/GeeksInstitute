"""
return
# Try to fetch to get ID
existing = MenuManager.get_by_name(name)
if not existing:
print("Item not found.")
return
if existing.delete():
print(f"Item '{name}' was deleted successfully.")
else:
print("There was an error deleting the item.")




def update_item_from_menu():
current_name = input("Current item name to update: ").strip()
if not current_name:
print("Name cannot be empty.")
return
existing = MenuManager.get_by_name(current_name)
if not existing:
print("Item not found.")
return


new_name = input(f"New name (leave empty to keep '{existing.name}'): ").strip() or existing.name
price_input = input(f"New price (leave empty to keep '{existing.price}'): ").strip()
if price_input == "":
new_price = existing.price
else:
try:
new_price = int(price_input)
except ValueError:
print("Invalid price. Use an integer.")
return


if existing.update(new_name, new_price):
print("Item was updated successfully.")
else:
print("There was an error updating the item.")




def show_restaurant_menu():
items = MenuManager.all_items()
if not items:
print("The restaurant menu is empty.")
return
print("\n--- Restaurant Menu ---")
for it in items:
print(f"{it.item_id:>3} | {it.name:<30} | {it.price:>5}")




def main_loop():
while True:
choice = show_user_menu()
if choice == 'V':
name = input("Name of the item to view: ").strip()
found = MenuManager.get_by_name(name)
if found:
print(found)
else:
print("Item not found.")
elif choice == 'A':
add_item_to_menu()
elif choice == 'D':
remove_item_from_menu()
elif choice == 'U':
update_item_from_menu()
elif choice == 'S':
show_restaurant_menu()
elif choice == 'Q':
print("Exiting. Final menu:")
show_restaurant_menu()
break
else:
print("Unknown option. Please choose a valid letter.")




if __name__ == '__main__':
main_loop()