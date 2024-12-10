from z3 import * 

e = Const('e', RealSort())
c = Const('c', RealSort())
g = Function('g', RealSort(), RealSort())
f = Function('f', RealSort(), RealSort(), RealSort())

gamma = []
gamma.append(f(f(e,e),e) == f(e,f(e,e)))
gamma.append(f(f(e,e),c) == f(e,f(e,c)))
gamma.append(f(f(e,c),e) == f(e,f(c,e)))
gamma.append(f(f(c,e),e) == f(c,f(e,e)))
gamma.append(f(f(e,c),c) == f(e,f(c,c)))
gamma.append(f(f(c,e),c) == f(c,f(e,c)))
gamma.append(f(f(c,c),e) == f(c,f(c,e)))
gamma.append(f(f(c,c),c) == f(c,f(c,c)))
gamma.append(And(f(e,e) == e, f(e,e) == e))
gamma.append(And(f(c,e) == c, f(e,c) == c))
gamma.append(And(f(e,g(e)) == e, f(g(e),e) == e))
gamma.append(And(f(c,g(c)) == e, f(g(c),c) == e))
gamma.append(And([(f(e,c) == e), (f(c,e) == e), Not(e == c)]))
gamma.append(And([(f(c,c) == c), (f(c,c) == c), Not(e == c)]))

s = Solver()
s.add(gamma)
print(s.check())