from problog.program import PrologString
from problog.formula import LogicFormula, LogicDAG
from problog.logic import Term
from problog.ddnnf_formula import DDNNF
from problog.cnf_formula import CNF



p = PrologString("""
coin(c1). coin(c2).
0.4::heads(C); 0.6::tails(C) :- coin(C).
win :- heads(C).
evidence(heads(c1), false).
query(win).
""")

lf = LogicFormula.create_from(p)   # ground the program

print(str(lf))

dag = LogicDAG.create_from(lf)     # break cycles in the ground program
cnf = CNF.create_from(dag)         # convert to CNF
ddnnf = DDNNF.create_from(cnf)       # compile CNF to ddnnf

ddnnf.evaluate()