def get_side_of_point(p, p1, p2):
    if p2[0] - p1[0] == 0:
        if p[1] < p1[1]:
            return -1
        elif p[1] > p1[1]:
            return 1
        else:
            return 0
    y = (p[0] - p1[0])*(p2[1]-p1[1]) /(p2[0] - p1[0]) + p1[1]
    if p[1] < y:
        return -1
    elif p[1] > y:
        return 1
    else:
        return 0

def is_on_triangle(p, A, B, C):
    if 0 in [get_side_of_point(p, A, B), get_side_of_point(p, B, C), get_side_of_point(p, C, A)]:
        return True
    if get_side_of_point(C, A, B) == get_side_of_point(p, A, B):
        if get_side_of_point(A, B, C) == get_side_of_point(p, B, C):
            if get_side_of_point(B, C, A) == get_side_of_point(p, C, A):
                return True
    return False


A = (1, 2)
B = (4, 6)
C = (6, 3)
D = (7, 4)
I = (3, 3)
H = (3, 4)
G = (2, 7)
print(is_on_triangle(D, A, B, C))