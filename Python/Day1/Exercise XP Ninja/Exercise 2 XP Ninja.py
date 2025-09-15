longest_sentence = ""  

while True:
    user_input = input("Enter the longest sentence you can without 'A' (or 'q' to quit): ")
    if user_input.lower() == "q":
        print(f"Game over! The longest valid sentence was:\n{longest_sentence}")
        break
    if "a" in user_input.lower():
        print("That sentence has an 'A'! Try again.")
        continue
    if len(user_input) > len(longest_sentence):
        longest_sentence = user_input
        print(f"Congratulations! New record with {len(user_input)} characters.")
    else:
        print("Good try, but not longer than your best yet.")



        
