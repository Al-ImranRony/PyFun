# Measure the execution time for small bits of python code

import timeit

# s = "-".join(map(str, range(100)))
# print(s)

print(timeit.timeit('"_".join(str(n) for n in range(100))', number=10000))

print(timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000))

print(timeit.timeit('"-".join(map(str, range(100)))', number=10000))
