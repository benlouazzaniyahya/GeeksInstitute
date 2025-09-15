user_input = input("Enter a word or string: ")
if user_input:
    result = user_input[0]
    for char in user_input[1:]:
        if char != result[-1]: 
            result += char
else:
    result = ""
print(f"Processed string: {result}")