!pip install ortools
from ortools.sat.python import cp_model

class CSPAgent:
    def __init__(self, model, variables):
        self.model     = model
        self.variables = variables

    def formulate_goal(self):
        return "Find values for A, B, C that satisfy all constraints"

    def act(self, environment):
        goal = self.formulate_goal()
        print(f"Agent goal : {goal}")
        return environment.solve(self.model, self.variables)

class Environment:
    def __init__(self):
        self.solver = cp_model.CpSolver()
        self.status = None

    def get_percept(self, model, variables):
        return {
            "num_variables"  : len(variables),
            "variable_names" : list(variables.keys()),
        }

    def solve(self, model, variables):
        percept = self.get_percept(model, variables)
        print(f"Percept    : {percept['num_variables']} variables "
              f"{percept['variable_names']}")
        self.status = self.solver.Solve(model)
        return self.status, self.solver

def run_agent(agent, environment):
    percept = environment.get_percept(agent.model, agent.variables)
    return agent.act(environment)

model = cp_model.CpModel()
A = model.new_int_var(0, 3, "A")
B = model.new_int_var(0, 3, "B")
C = model.new_int_var(0, 3, "C")
model.add(A != B)
model.add(B != C)
model.add(A + B <= 4)
variables   = {"A": A, "B": B, "C": C}
agent       = CSPAgent(model, variables)
environment = Environment()
print("=" * 45)
print("Task 4 — Basic CSP Modelling (OR-Tools)")
print("=" * 45)
status, solver = run_agent(agent, environment)
print()
print("=" * 45)
print("CSP Definition")
print("=" * 45)
print("  Variables : A, B, C")
print("  Domain    : {0, 1, 2, 3}")
print("  Constraints:")
print("    1. A ≠ B")
print("    2. B ≠ C")
print("    3. A + B ≤ 4")
print()
print("=" * 45)
print("Solver Result")
print("=" * 45)
if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
    a_val = solver.value(A)
    b_val = solver.value(B)
    c_val = solver.value(C)
    print(f"  Status : {'OPTIMAL' if status == cp_model.OPTIMAL else 'FEASIBLE'}")
    print()
    print(f"  A = {a_val}")
    print(f"  B = {b_val}")
    print(f"  C = {c_val}")
    print()
    print("  Constraint verification:")
    print(f"    A ≠ B     →  {a_val} ≠ {b_val}          "
          f"→  {'✓ satisfied' if a_val != b_val else '✗ violated'}")
    print(f"    B ≠ C     →  {b_val} ≠ {c_val}          "
          f"→  {'✓ satisfied' if b_val != c_val else '✗ violated'}")
    print(f"    A + B ≤ 4 →  {a_val} + {b_val} = {a_val + b_val} ≤ 4  "
          f"→  {'✓ satisfied' if a_val + b_val <= 4 else '✗ violated'}")
    print()
    print(f"  Solver wall time : {solver.wall_time:.4f} s")
    print(f"  Branches explored: {solver.num_branches}")
else:
    print("  Status : NO SOLUTION EXISTS")
    print("  The constraints cannot be satisfied over domain {0, 1, 2, 3}.")
