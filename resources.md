# Resources

These are the main resources I used while learning about reference counting and garbage collection in CPython.

## Python `sys.getrefcount()` Documentation

Python 3.12 documentation for `sys.getrefcount()`.

I used this to understand why `sys.getrefcount(a)` usually returns a value that is one higher than expected. The documentation explains that calling `getrefcount()` temporarily creates an extra reference to the object. It also explains that, immortal objects can have very large reference counts that do not represent the actual number of references.

Source:
https://docs.python.org/3.12/library/sys.html#sys.getrefcount

## Python `gc` Module Documentation

Python 3.12 documentation for the garbage collector interface.

I used this to understand how CPython's cyclic garbage collector works alongside reference counting. The documentation explains that the cyclic garbage collector supplements Python's reference counting and can be disabled with `gc.disable()`. It also helped me understand that automatic garbage collection does not necessarily happen immediately when a reference cycle becomes unreachable.

Source:
https://docs.python.org/3.12/library/gc.html

## Python C API Reference Counting Documentation

Python 3.12 C API documentation for reference counting.

Used this to learn more about how CPython handles reference counts internally. It describes functions such as `Py_INCREF()` and `Py_DECREF()`, which are used when references to Python objects are acquired and released.

Source:
https://docs.python.org/3.12/c-api/refcounting.html

## PEP 683: Immortal Objects

PEP 683 explains the immortal objects feature introduced in Python 3.12.

I used this after getting a very large value from:

```python
sys.getrefcount(10)

This helped me understand why some objects can have extremely large reference counts. In Python 3.12, CPython can treat certain objects as immortal, meaning their displayed reference counts do not behave like normal object reference counts.