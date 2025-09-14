month=int(input("input a month (1 to 12)"))
if month>=3 and month<=5:
    print("Spring")
elif month>=6 and month<=8:
    print("Summer")
elif month>=9 and month<=11:
    print("Autumn")
elif month==12 or month<=2:
    print("Winter")
else: 
    print("Invalid Mont")