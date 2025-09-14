ListNumbers=[]
for i in range(1,4):
    ListNumbers.append(int(input(f"Enter the number {i}:")))
    print(f"{ListNumbers[i-1]} \n")

GreatestNumber=max(ListNumbers)
print(f"The greatest Number is:{GreatestNumber}")
    