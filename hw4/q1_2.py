from z3 import * 

e = Const('e', RealSort())
c = Const('c', RealSort())
d = Const('d', RealSort())
g = Function('g', RealSort(), RealSort())
f = Function('f', RealSort(), RealSort(), RealSort())

gamma = []


gamma.append(f(f(e,e),e) == f(e,f(e,e)))
gamma.append(f(f(c,c),c) == f(c,f(c,c)))
gamma.append(f(f(d,d),d) == f(d,f(d,d)))
gamma.append(f(f(e,e),c) == f(e,f(e,c)))
gamma.append(f(f(e,c),e) == f(e,f(c,e)))
gamma.append(f(f(c,e),e) == f(c,f(e,e)))
gamma.append(f(f(e,c),c) == f(e,f(c,c)))
gamma.append(f(f(c,e),c) == f(c,f(e,c)))
gamma.append(f(f(c,c),e) == f(c,f(c,e)))
gamma.append(f(f(e,e),d) == f(e,f(e,d)))
gamma.append(f(f(e,d),e) == f(e,f(d,e)))
gamma.append(f(f(d,e),e) == f(d,f(e,e)))
gamma.append(f(f(e,d),d) == f(e,f(d,d)))
gamma.append(f(f(d,e),d) == f(d,f(e,d)))
gamma.append(f(f(d,d),e) == f(d,f(d,e)))
gamma.append(f(f(c,c),d) == f(c,f(c,d)))
gamma.append(f(f(c,d),c) == f(c,f(d,c)))
gamma.append(f(f(d,c),c) == f(d,f(c,c)))
gamma.append(f(f(c,d),d) == f(c,f(d,d)))
gamma.append(f(f(d,c),d) == f(d,f(c,d)))
gamma.append(f(f(d,d),c) == f(d,f(d,c)))
gamma.append(f(f(e,c),d) == f(e,f(c,d)))
gamma.append(f(f(e,d),c) == f(e,f(d,c)))
gamma.append(f(f(c,d),e) == f(c,f(d,e)))
gamma.append(f(f(c,e),d) == f(c,f(e,d)))
gamma.append(f(f(d,c),e) == f(d,f(c,e)))
gamma.append(f(f(d,e),c) == f(d,f(e,c)))

gamma.append(And(f(c,e) == c, f(e,c) == c))
gamma.append(And(f(d,e) == d, f(e,d) == d))
gamma.append(And(f(e,e) == e, f(e,e) == e))

gamma.append(And(f(c,g(c)) == e, f(g(c),c) == e)) 
gamma.append(And(f(e,g(e)) == e, f(g(e),e) == e)) 
gamma.append(And(f(d,g(d)) == e, f(g(d),d) == e)) 

gamma.append(Or([(f(c,d) == e), (f(d,c) == e), Not(d == g(c))]))

print(len(gamma))

s = Solver()
s.add(gamma)
print(s.check())
print(s.model())