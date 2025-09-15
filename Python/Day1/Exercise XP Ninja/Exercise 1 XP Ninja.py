>>> 3 <= 3 < 9                       True

>>> 3 == 3 == 3                      True

>>> bool(0)                          False

>>> bool(5 == "5")                   False

>>> bool(4 == 4) == bool("4" == "4") True

>>> bool(bool(None))                 False

x = (1 == True)                      True
y = (1 == False)                     False
a = True + 4                         5
b = False + 10                       10

print("x is", x)                     True
print("y is", y)                     False
print("a:", a)                       5
print("b:", b)                       10