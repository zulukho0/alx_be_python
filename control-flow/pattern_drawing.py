uInput = int(input("Enter the size of the pattern: "))

i = 0
while i < uInput:
    for asterisk in range(uInput):
        print("*", end="")
    print()
    i += 1