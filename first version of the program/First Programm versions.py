a=int(input("1/2: "))
if a == "1" or "nether":
    x = int(input("X coordinates: "))
    z = int(input("Z coordinates: "))
    x_1 = x/8
    z_2 = z/8
    print(x_1)
    print(z_2)
elif a == "2" or "over":
    x = int(input("X coordinates: "))
    z = int(input("Z coordinates: "))
    x_1 = x * 8
    z_2 = z * 8
    print(x_1)
    print(z_2)
else:
    print("wrong coordinate entered")