# levels of list comprehension

# level 1:
fullName = "Imran Rony"
chars = [char for char in fullName]
print(fullName, chars)

Matrix = [[2, 1, 5],
          [5, 99, 0],
          [33, 2, 4]]
rowMax = [max(row) for row in Matrix]
print(rowMax)


# level 2:
peoples = ["Imran", "Rony", "jerry", "Tom", "Bean", "Yang"]
p1 = [name for name in peoples if name.startswith('Y')]
p2 = [name for name in peoples if name.startswith('Y') or len(name) < 4]
p3 = [name for name in peoples if len(name) > 4 and name.islower()]
print(p1, p2, p3)


# level 3:
peoples = ["Imran", "Rony", "jerry", "Tom", "Bean", "Yang"]
p1 = [name.capitalize() for name in peoples if name.startswith('j')]
print(p1)
p2 = [name if name.startswith('Y') else 'Not Genius' for name in peoples]
print(p2)


# level 4:
peoples = ["Imran", "Rony", "jerry", "Tom", "Bean", "Yang"]
p1 = [char for name in peoples for char in name]
print(p1)
p2 = [char for name in peoples if len(name) < 4 for char in name]
print(p2)


# level 5: Avoid Higher Order Functions for Readability
peoples = ["Imran", "Rony", "jerry", "Tom", "Bean", "Yang"]
p1 = filter(lambda a: len(a) < 4, peoples)
print(list(p1))
p2 = [a for a in peoples if len(a) < 4]
print(p2)


# level 6: Use Generator Expressions to Reduce Memory Costs
large_list = [x for x in range(1_000_000)]
large_list_g = (x for x in range(1_000_000))
print(large_list.__sizeof__())
print(large_list_g.__sizeof__())