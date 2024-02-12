# An Interesting Problem

## The Premise
We start with 2 lists of consecutive integers A and B, a function f, and some
upper and lower bounds. For each pair of integers (a, b) where a is in A and
b is in B we want to count how many, after applying the function f, are
within the bounds.

## Solutions

### Brute Force
Brute force is the canonical solution, and the only solution that works for
all f. The code in [naive_method.py](./naive_method.py) is an implementation of this solution.

### Addition Solution
For f(x, y) = x + y there is fairly simple solution that can run in O(1)
time. If you count the number of occurences of for a given number and plot
the count againts the value, the distribution forms a trapezoid. From that
it is fairly simple to derive the area given some upper and lower bounds.

After outlining the general idea of this solution, the original problem
poser created an implementation in R, but I have opted not to implement this
method, as there is a more general method.

### Slice Intersection Method
This is a fairly general method that for a lot of functions f can reduce the
problem from quadratic to linear time. Where the brute force method
calculates whether a point (a, b) should be counted or not, the slice
intersecction method tries to count as much of a line, i.e. a fixed value of
a, as possible at once. By finding y where f(a, y) intersects with the upper
and lower bounds the segments between each intersection can be counted all
at once. Thus, for simple f this is a constant time check. 

The implementation I have provided in [slice_intersection_method.py](./slice_intersection_method.py) requires
that an additional f_intersect method is provided, that can calculate the
intersection points. This is to reduce the amount of work to get this
demonstration working, whilst still providing flexibility. For example, even
though the idea is based on "intersections" this method can work perfectly
fine for discontinuous functions with intelligent implementation of
f_intersect.

With some very rudimentary experiments I was able to conclude that I can't
be bothered running the brute force method very long to get comparisons with
the slice intersection method. The longest test I ran is in the main.py file
where the brute force took 147 seconds, while the slice intersection took
0.09 seconds, or approximately 1600x speed improvement.
