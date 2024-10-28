from z3 import *

def intersect(l1, u1, l2, u2):
    x = Real('x')
    return Exists(x, And([l1<x, x<u1, l2<x, x<u2]))

def not_eq(l1, u1, l2, u2):
    return Not(And([l1==u1, l2==u2]))

l1, u1, l2, u2, l3, u3, l4, u4 = Reals('l1 u1 l2 u2 l3 u3 l4 u4')

distinct = And([not_eq(l1, u1, l2, u2), not_eq(l1, u1, l3, u3), not_eq(l1, u1, l4, u4), not_eq(l2, u2, l3, u3), not_eq(l3, u3, l4, u4)])
inters = And([intersect(l1, u1, l2, u2), intersect(l1, u1, l4, u4), intersect(l2, u2, l3, u3), intersect(l3, u3, l4, u4), Not(intersect(l1, u1, l3, u3)), Not(intersect(l2, u2, l4, u4))])

phi = Exists([l1, u1, l2, u2, l3, u3, l4, u4], And(inters, distinct))

s = Solver()
s.add(phi)
c = s.check()
print(c)



