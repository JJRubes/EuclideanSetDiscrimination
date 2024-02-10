import time

"""
     *** Koun no nekomata's puzzle ***
"""

"""
Brute force general solution
works for all f(x: int, y: int) -> int
"""
def naive_bounded_count(aLB, aUB, bLB, bUB, cLB, cUB, f):
    count = 0
    for i in range(aLB, aUB + 1):
        for j in range(bLB, bUB + 1):
            if cLB <= f(i, j) <= cUB:
                print("x", end=" ")
                count += 1
            else:
                print(".", end=" ")
        print("")
    return count



"""
If you can provide a list of intersections with the upper and lower bound
for a given slice of the surface then you only need to iterate through one direction

f_intersect(x: int, C_lb: int, C_ub: int) -> int
returns a list of y coordinates such that f(x, y) = C_lb or f(x, y) = C_ub
"""
class DistCounter:
    def __init__(self, A_lb, A_ub, B_lb, B_ub, C_lb, C_ub, f, f_intersect):
        self.A_lb = A_lb
        self.A_ub = A_ub
        self.B_lb = B_lb
        self.B_ub = B_ub
        self.C_lb = C_lb
        self.C_ub = C_ub
        self.f = f
        self.f_intersect = f_intersect

    # As it iterates over all of the values in A,
    # it probably makes sense to make it so |A| <= |B|
    def count_in_range(self):
        count = 0
        for x in range(self.A_lb, self.A_ub + 1):
            bounded_intersections = self.get_bounded_intersections(x)
            count += self.count_slice_by_intersections(x, bounded_intersections)
        return count

    def count_slice_by_intersections(self, x, bounded_intersections):
        count = 0
        current_position = self.B_lb
        is_in_range = self.in_range(x, self.B_lb)
        for next_intersection in bounded_intersections:
            # handle multiple intersections between consecutive integers
            if int(next_intersection) < current_position:
                continue
            if is_in_range:
                # if you start in range, you will stay in range until
                # you reach another intersection
                count += int(next_intersection) - current_position + 1
            current_position = int(next_intersection) + 1
            is_in_range = self.in_range(x, current_position)
        if is_in_range and current_position <= self.B_ub:
            count += self.B_ub - current_position + 1
        return count

    def get_bounded_intersections(self, x):
        intersections = self.f_intersect(x, self.C_lb, self.C_ub)
        intersections.sort()
        intersections = [y for y in intersections if self.B_lb <= y <= self.B_ub]
        return intersections

    def in_range(self, x, y):
        return self.C_lb <= self.f(x, y) <= self.C_ub


"""
Verifying that it works
"""
if __name__ == "__main__":
    def f(x, y):
        return x * y

    def f_intersect(x, C_lb, C_ub):
        # f(x, y) = x * y
        # y = f(x, y) / x
        if x == 0:
            return []
        return [C_lb / x, C_ub / x]

    # A_lb = -50000
    # A_ub = 50000
    # B_lb = -10000
    # B_ub = 90000
    # C_lb = -123
    # C_ub = 456

    A_lb = -2
    A_ub = 8
    B_lb = 5
    B_ub = 12
    C_lb = 6
    C_ub = 30

    start = time.time()
    naive_count = naive_bounded_count(A_lb, A_ub, B_lb, B_ub, C_lb, C_ub, f)
    naive_time = time.time() - start
    print("Naive Method:")
    print(f"Count: {naive_count}, Time: {naive_time}\n")

    dc = DistCounter(A_lb, A_ub, B_lb, B_ub, C_lb, C_ub, f, f_intersect)
    start = time.time()
    smart_count = dc.count_in_range()
    smart_time = time.time() - start
    print("Complicated Method:")
    print(f"Count: {smart_count}, Time: {smart_time}")
