import gc
import weakref


class Node:
    pass


gc.disable()

a = Node()
b = Node()

a.other = b
b.other = a

a_ref = weakref.ref(a)
b_ref = weakref.ref(b)

print("Before deleting names:")
print("a alive:", a_ref() is not None)
print("b alive:", b_ref() is not None)

del a
del b

print("\nAfter deleting names, before garbage collection:")
print("a alive:", a_ref() is not None)
print("b alive:", b_ref() is not None)

collected = gc.collect()

print("\nAfter gc.collect():")
print("Objects collected:", collected)
print("a alive:", a_ref() is not None)
print("b alive:", b_ref() is not None)

gc.enable()