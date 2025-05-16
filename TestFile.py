from DataManipulation  import FinanceAnthology as fa



print(fa.TimeValueSolver(None, 20,.05, 2,1))
print(fa.TimeValueSolver(22.05, None,.05, 2,1))
print(fa.TimeValueSolver(22.05, 20,None, 2,1))
print(fa.TimeValueSolver(22.05, 20,.05, None,1))
print(fa.TimeValueSolver(24.31, 20,.05, 2,None))


