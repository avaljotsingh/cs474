from z3 import *

x, y, z = Consts('x y z', RealSort())
f = Function('f', RealSort(), RealSort())

phi = And([y<=x, x<=y, f(y)==f(7), x<=5])
s = Solver()
s.add(phi)
print(s.check())
print(s.model())