import sys

a = [10, 20, 30]
print("After creating a:", sys.getrefcount(a))

b = a
print("After b = a:", sys.getrefcount(a))

c = a
print("After c = a:", sys.getrefcount(a))

del c
print("After deleting c:", sys.getrefcount(a))

del b
print("After deleting b:", sys.getrefcount(a))