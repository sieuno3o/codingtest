def solution(a, b):
    aa = int(str(a)+str(b))
    bb = int(str(b)+str(a))
    return aa if aa > bb else bb  