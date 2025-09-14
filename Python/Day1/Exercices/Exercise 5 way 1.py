my_fav_numbers={10,7,20,89}
n1=int(input("Add the first number to the set:\n"))
n2=int(input("Add the second number to the set:\n"))
my_fav_numbers.add(n1)
my_fav_numbers.add(n2)
print("All numbers:", my_fav_numbers)
my_fav_numbers.remove(n2)
print("All numbers after remove the last number entered:", my_fav_numbers)
friend_fav_numbers={10,80,9}
our_fav_numbers=my_fav_numbers.union(friend_fav_numbers)
print("All Favorite numbers concatinated with friend fevorite numbers :", our_fav_numbers)

