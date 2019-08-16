# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```
a)  a = 0                   #O(1)
    while (a < n * n * n):  #O(n * n * n)
      a = a + n * n         #O(1)
```
*O(n)*

```
b)  sum = 0                                 #O(1)
    for i in range(n):                      #O(n)
      i += 1                                #O(1)
      for j in range(i + 1, n):             #O(n)
        j += 1                              #O(1)
        for k in range(j + 1, n):           #O(n)
          k += 1                            #O(1)
          for l in range(k + 1, 10 + k):    #O(10)
            l += 1                          #O(1)
            sum += 1                        #O(1)
```
b) *O(n^3)*
```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
*O(n)*

## Exercise II

Suppose that you have an _n_-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor _f_ or higher, and doesn't get broken if dropped off a floor less than floor _f_. Devise a strategy to determine the value of _f_ such that the number of dropped eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode and give the runtime complexity of your solution.

####Answer
If a build is n stories tall and an egg gets broken if it's thrown off floor f or high then keep all eggs at floor f or lower

```
def break_egg(n, f, e):
    # n is the number of stories in a building
    # f is the break point of the egg
    # e is the story that the egg is being thrown from

    if f >= n:
        return "The break point of the egg is taller than the building:
    else:
        if e < f:
            return "Egg will NOT break"
        else:
            return  "Egg will break"
```

The ideal strategy would be to keep all eggs on floor f or lower or keep all eggs in a building that has n < f floors so that regardless of the floor number in the building it is less than the break point of the egg. This would be a constant time or O(1) algorithm comparing f the break point of the egg and n the number of stories in a building.