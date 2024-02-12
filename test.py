import time
from naive_method import naive_bounded_count
from slice_intersect_method import DistCounter

def test(
        test_name,
        params,
        functions
    ):
    A_lb, A_ub, B_lb, B_ub, C_lb, C_ub = params
    f, f_intersect = functions
    print(f"Test \"{test_name}\": ", end="")
    naive_count = naive_bounded_count(
            A_lb,
            A_ub,
            B_lb,
            B_ub,
            C_lb,
            C_ub,
            f
        )
    dc = DistCounter(
            A_lb,
            A_ub,
            B_lb,
            B_ub,
            C_lb,
            C_ub,
            f,
            f_intersect
        )
    slice_intersect_count = dc.count()
    if naive_count == slice_intersect_count:
        print("pass")
    else:
        print(f"failed {naive_count} != {slice_intersect_count}")


def f_add(x, y):
    return x + y


def f_int_add(x, C_lb, C_ub):
    # f(x, y) = x + y
    # y = f(x, y) - x
    return [C_lb - x, C_ub - x]


def f_mult(x, y):
    return x * y


def f_int_mult(x, C_lb, C_ub):
    # f(x, y) = x * y
    # y = f(x, y) / x
    if x == 0:
        return []
    return [C_lb / x, C_ub / x]


def f_max(x, y):
    return max(x, y)


def f_int_max(x, C_lb, C_ub):
    intersections = []
    if x < C_lb:
        intersections.append(C_lb)
    if x <= C_ub:
        intersections.append(C_ub)
    return intersections


def f_other(x, y):
    return x * (x + y)


def f_int_other(x, C_lb, C_ub):
    # f(x, y) = x * (x + y)
    # f(x, y) / x = x + y
    # y = f(x, y) / x - x
    if x == 0:
        return []
    return [C_lb / x - x, C_ub / x - x]


if __name__ == "__main__":
    functions = [
            ("add", (f_add, f_int_add)),
            ("multiply", (f_mult, f_int_mult)),
            ("max", (f_max, f_int_max)),
            ("linear", (f_other, f_int_other))
        ]
    params = [
            ("smallest", (-2, 8, 5, 12, 6, 30)),
            ("small", (-50, 50, -10, 90, -123, 456)),
            ("medium (small bound)", (-1000, 1000, -200, 1800, -123, 456)),
            ("medium (big bound)", (-1000, 1000, -200, 1800, -1025, 4500)),
            ("big", (-5000, 5000, -1000, 9000, -4238, 1055))
        ]
    for p in params:
        for f in functions:
            test(f[0] + " " + p[0], p[1], f[1])
