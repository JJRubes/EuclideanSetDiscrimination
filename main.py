import time
from naive_method import naive_bounded_count
from slice_intersect_method import DistCounter

def f(x, y):
    return 2 * x * x + x * y


def f_intersect(x, C_lb, C_ub):
    # f(x, y) = 2 * x * x + x * y
    # y = (f(x, y) - 2 * x * x) / x
    if x == 0:
        return []
    return [(C_lb - 2 * x * x) / x, (C_ub - 2 * x * x) / x]


if __name__ == "__main__":
    A_lb = -16000
    A_ub = 16000
    B_lb = -1600
    B_ub = 14400
    C_lb = -1738
    C_ub = 2601

    dc = DistCounter(A_lb, A_ub, B_lb, B_ub, C_lb, C_ub, f, f_intersect)
    print("Slice Intersect Method:")
    start = time.time()
    slice_intersect_count = dc.count()
    slice_intersect_time = time.time() - start
    print(f"Count: {slice_intersect_count}, Time: {slice_intersect_time}\n")

    print("Naive Method:")
    start = time.time()
    naive_count = naive_bounded_count(A_lb, A_ub, B_lb, B_ub, C_lb, C_ub, f)
    naive_time = time.time() - start
    print(f"Count: {naive_count}, Time: {naive_time}")
