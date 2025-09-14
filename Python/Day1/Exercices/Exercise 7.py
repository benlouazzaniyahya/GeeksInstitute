basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
print("here is table removed a banana and Blueberries words:",basket)
basket.append("Kiwi")
basket.append("Apples")
print("here is table after adding kiwi and apples words:",basket)
number=basket.count("Apples")
print(f"we have {number} apples")