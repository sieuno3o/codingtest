def solution(sides):
    sides.sort()
    if sides[2] >= sides[0] + sides[1]:
        return 2
    return 1