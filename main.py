set_A = set()
set_B = set()

while True:
    item_A = input("Please input set A (type End to End): ")
    item_A = item_A.capitalize()

    if item_A == "End":
        break
    else:
        set_A.add(item_A)

print("")

while True:
    item_B = input("Please input set B (type End to End): ")
    item_B = item_B.capitalize()

    if item_B == "End":
        break
    else:
        set_B.add(item_B)

intersection = set_A.intersection(set_B)

print("Intersection of A and B is: ", intersection)

quit()