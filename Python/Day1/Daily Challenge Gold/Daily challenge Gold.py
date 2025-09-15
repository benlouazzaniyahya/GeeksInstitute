from datetime import datetime

# Ask the user for their birthdate
birthdate_str = input("Enter your birthdate (DD/MM/YYYY): ")

# Convert the input string to a datetime object
birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")
today = datetime.today()

# Calculate age
age = today.year - birthdate.year
# Adjust if birthday hasn't happened yet this year
if (today.month, today.day) < (birthdate.month, birthdate.day):
    age -= 1

# Determine the number of candles (last digit of age)
num_candles = age % 10
candles = "i" * num_candles

# Function to print the cake
def print_cake():
    print(f"       ___{candles}___")
    print("      |:H:a:p:p:y:|")
    print("    __|___________|__")
    print("   |^^^^^^^^^^^^^^^^^|")
    print("   |:B:i:r:t:h:d:a:y:|")
    print("   |                 |")
    print("   ~~~~~~~~~~~~~~~~~~~\n")

# Check for leap year bonus
if (birthdate.year % 4 == 0 and birthdate.year % 100 != 0) or (birthdate.year % 400 == 0):
    print("🎉 Bonus: You were born in a leap year! Here's two cakes! 🎉\n")
    print_cake()
    print_cake()
else:
    print_cake()

# Display age
print(f"Happy {age}th Birthday!")
