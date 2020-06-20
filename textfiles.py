
oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"]

with open("C:/data/oceans.txt", "w") as f:
    for ocean in oceans:
        print(ocean, file=f)

with open("C:/data/oceans.txt", "a") as f:
    print(23*"=", file=f)
    print("There are the 5 oceans.", file=f)