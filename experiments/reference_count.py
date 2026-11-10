import sys

a = [1, 2, 3]

print("After creating a:", sys.getrefcount(a))

b = a
print("After b = a:", sys.getrefcount(a))

del b
print("After deleting b:", sys.getrefcount(a))