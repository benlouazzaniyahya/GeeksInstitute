sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
print("The deli has run out of pastrami")
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
finished_sandwiches=[]
while sandwich_orders:
    sandwich=sandwich_orders.pop(0)
    finished_sandwiches.append(sandwich)
print("All madded sandwiches are:",finished_sandwiches)
