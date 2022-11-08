# Short Circuiting

This technique relates to the stoppage of a boolean operation if a certain condition has already been met, i.e. the program moves on if it is happy, without the need to evaluate what follows.

## or

```
x = 3
y = 2
b = 1

result = if x > y or y < b:

print(result)

```

In the above example we can see that the first condition (`x > y`) is true so the program short circuits and discards evaluating the second condition.


## and


