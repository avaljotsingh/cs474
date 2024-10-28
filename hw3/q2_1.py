from z3 import *

l1, u1, l2, u2, z, w = Reals('l1 u1 l2 u2 z w')

p = And([l1<z, z<u1, l2<z, z<u2])
q = Exists(w, And([l1<w, w<u1, l2<w, w<u2]))
phi = ForAll(z, Implies(p, q))

qe_phi = simplify(Tactic('qe')(phi).as_expr())

print(qe_phi)




