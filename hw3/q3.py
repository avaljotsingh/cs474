from z3 import *

x, y = Reals('x y')

phi = And(2*y>3*x, 4*y<8*x+10)
psi = ForAll(x, Exists(y, phi))

qe_psi = Tactic('qe')(psi).as_expr()
print(qe_psi)



