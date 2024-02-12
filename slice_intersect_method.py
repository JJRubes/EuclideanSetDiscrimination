from math import floor
debug = 0

"""
If you can provide a list of intersections with the upper and lower bound
for a given slice of the surface then you only need to iterate through one
direction

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
    def count(self):
        count = 0
        for x in range(self.A_lb, self.A_ub + 1):
            bounded_intersections = self.get_bounded_intersections(x)
            count += self.count_slice(x, bounded_intersections)
        return count

    def count_slice(self, x, bounded_intersections):
        if debug > 1:
            print(f"Slice: {x}, intersections {bounded_intersections}")
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
                additional = floor(next_intersection) - current_position + 1
                count += additional
            elif floor(next_intersection) == next_intersection:
                # if next_intersection is a whole number then it 
                # won't be counted unless we have this case
                count += 1

            current_position = floor(next_intersection) + 1
            is_in_range = self.in_range(x, current_position)

        if is_in_range and current_position <= self.B_ub:
            count += self.B_ub - current_position + 1
        if debug > 0:
            print(f"Slice {x}, count {count}")
        return count

    def get_bounded_intersections(self, x):
        intersections = self.f_intersect(x, self.C_lb, self.C_ub)
        intersections.sort()
        return [y for y in intersections if self.B_lb <= y <= self.B_ub]

    def in_range(self, x, y):
        return self.C_lb <= self.f(x, y) <= self.C_ub
