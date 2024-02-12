debug = 0

"""
Brute force general solution
works for all f(x: int, y: int) -> int
"""
def naive_bounded_count(aLB, aUB, bLB, bUB, cLB, cUB, f):
    count = 0
    for i in range(aLB, aUB + 1):
        inner_count = 0
        for j in range(bLB, bUB + 1):
            if cLB <= f(i, j) <= cUB:
                if debug > 1:
                    print("x", end=" ")
                inner_count += 1
            elif debug > 1:
                    print(".", end=" ")
        count += inner_count
        if debug > 0:
            print(inner_count)
    return count
