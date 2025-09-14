names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

i=0
NamesLower=[name.lower() for name in names]
while i==0:
    UserName=input("Type the Name \n")
    if UserName.lower() in NamesLower:
        indexe=NamesLower.index(UserName.lower())
        print(f"The entered Name {UserName} with the index {indexe} exist in the list")
        i=1
    else:
        print(f"The typed Name {UserName} is not in the list")
    
        