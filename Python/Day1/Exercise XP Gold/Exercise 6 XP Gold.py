import random
wins=0
losses=0
number=10
rand=0
while True :
    state=input("Type a number from 1 to 9 or if you want exit please 0 \n")
    if state.isdigit():
        number=int(state)
        if number>=0 and number<=9:
            if random.randint(1,9)==number:
                print("Winner")
                wins += 1
        if random.randint(1,9)!=number: 
                print("Better luck next time")
                losses += 1 
        if number==0:
                break

print("You finished your Game")
print(f"Total Wins:{wins}")
print(f"Total Loses:{losses}")
