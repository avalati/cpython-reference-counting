# cpython-reference-counting

For my COMP 211 Checkoff 3 project, I explored how CPython manages memory using reference counting.

In COMP 211, we learned how memory management works in C. In C, the programmer has to manually manage memory using functions like `malloc()` and `free()`. I wanted to learn how Python manages memory without the programmer having to manually free every object.

## What I Explored

I focused on reference counting in CPython, which is the main implementation of Python.

Reference counting keeps track of how many references point to an object. When a new reference is created, the reference count increases. When a reference is removed, the reference count decreases.

When an object's reference count reaches zero, CPython can reclaim the memory used by that object.

I also explored a problem with reference counting called reference cycles and how CPython handles them.

## Experiment 1: Reference Counting

My first experiment uses Python's `sys.getrefcount()` function to see how the reference count of an object changes.

The program starts by creating a list:

```python
a = [1, 2, 3]
```

Then another variable points to the same list:

```python
b = a
```

Now both `a` and `b` reference the same object, so the reference count increases.

Then I remove `b`:

```python
del b
```

The reference count decreases because there is one less reference pointing to the list.

One thing I found interesting is that `sys.getrefcount()` temporarily adds another reference while checking the object. Because of this, the value it prints can be one higher than expected.

The code for this experiment is located in:

```text
experiments/reference_count.py
```

## Experiment 2: Reference Cycles

My second experiment explores a weakness of reference counting.

I created two objects that reference each other:

```python
a.other = b
b.other = a
```

This creates a reference cycle.

Even after deleting the names `a` and `b`, the two objects still reference each other. This means reference counting alone cannot immediately reclaim them.

To show this, I disabled automatic garbage collection before creating the cycle.

After deleting `a` and `b`, I checked whether the objects were still alive. Both objects were still there.

I then manually ran:

```python
gc.collect()
```

After `gc.collect()` ran, the two unreachable objects were collected.

This experiment showed me why CPython needs more than just reference counting. It also has a cyclic garbage collector to handle unreachable reference cycles.

The code for this experiment is located in:

```text
experiments/reference_cycle.py
```

## Connection to C

This topic connects to memory management in C.

In C, the programmer is responsible for manually freeing dynamically allocated memory.

For example:

```c
int *p = malloc(sizeof(int));
free(p);
```

If memory is not freed correctly, problems such as memory leaks can happen.

In CPython, the programmer usually does not manually free objects. Reference counting and garbage collection help manage memory automatically.

## What I Found Most Interesting

The most interesting thing I learned was that CPython does not manage memory using only one method.

Reference counting handles many objects, but it has problems with reference cycles. Because of this, CPython also uses a cyclic garbage collector.

I also found it interesting that `del` does not necessarily delete an object. It removes a reference to the object. If another reference still exists, the object can stay alive.

## How to Run the Experiments

To run the reference counting experiment:

```bash
python3 experiments/reference_count.py
```

To run the reference cycle experiment:

```bash
python3 experiments/reference_cycle.py
```

## Project Structure

```text
cpython-reference-counting/
├── README.md
├── experiments/
│   ├── reference_count.py
│   └── reference_cycle.py
├── presentation/
└── resources.md
```

The `experiments` folder contains the Python programs I created while exploring the topic.

The `presentation` folder will contain my presentation materials.

The `resources.md` file contains the sources and documentation I used while learning about reference counting and garbage collection.

## Resources

The resources used for this project are listed in `resources.md`.