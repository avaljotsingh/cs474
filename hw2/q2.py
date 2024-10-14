from z3 import *

p, q, r = Bools('p q r')

phi = And([Or(q, Not(r)), Or(Not(p), r), Or(Not(q), Or(r, p)), Or(p, Or(q, Not(q))), Or(Not(r), q)])
psi = And([Or(Not(r), q), Or(Not(p), r), Or(Not(q), Or(p, r)), Or(Not(p), q), Or(Not(q), r)])

print(f"phi is \n{phi}\n\n")
print(f"psi is \n{psi}\n\n")


print('phi is satisfiable')
s = Solver()
s.add(phi)
print(s.check())

print()

print('phi and psi are equivalent')
s = Solver()
formula = And(Implies(phi, psi), Implies(psi, phi))
s.add(Not(formula))
print(s.check())

