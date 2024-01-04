r1 = int(input("Start of the range: "))
r2 = int(input("End of the range: "))

# Normal pyramid pattern printing
print("Normal Pyramid:")
for i in range(r1, r2 + 1):
    spaces = " " * (r2 - i)
    stars = "* " * i
    print(spaces + stars)

# Inverted pyramid pattern printing
print("\nInverted Pyramid:")
for i in range(r2, 0, -1):
    spaces = " " * (r2 - i)
    stars = "* " * i
    print(spaces + stars)