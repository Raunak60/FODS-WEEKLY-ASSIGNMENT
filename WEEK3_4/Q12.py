# Set operations.

set1, set2 = {20, 40, 60}, {10, 20, 30, 40, 50, 60}
print("Union:", set1 | set2, "Length:", len(set1 | set2))
print("Intersection:", set1 & set2)
print("Symmetric Difference:", set1 ^ set2)
set1.add(40)
set2.remove(20)
print("Updated Set1:", set1)
print("Updated Set2:", set2)
