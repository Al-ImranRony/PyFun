# Convert weights using python

weight  = int(input("Weight: "))
unit = input("lb or kg ?: ")

if unit == "lb": print("~Converting to kg unit...~~>")
else:             print("~Converting to lbs unit...~~>")

if unit.lower() == 'lb':
    conv = weight * 0.45
    print(f"Your are {round(conv, 2)} kelos !")
else:
    conv = weight / 0.45
    print(f"Your are {round(conv, 2)} pounds !")