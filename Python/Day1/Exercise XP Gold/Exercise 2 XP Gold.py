print("------------All numbers from 1 to 20 listing with there index------------")
for i in range(1,21):
    print(f"Number,{i} and his index is {i-1}")
print(f"Number,{i} and his index is {i-1}") 
print("------------All numbers from 1 to 20 listing that has even index------------")
for i in range(1,21):
    if (i-2)%2==0:
        print(f"Number,{i} has an even index {i-1}")
    