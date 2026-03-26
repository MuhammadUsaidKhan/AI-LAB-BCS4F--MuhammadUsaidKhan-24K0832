!pip install ortools
from ortools.sat.python import cp_model

class OptimizationAgent:
    def __init__(self, model, variables):
        self.model     = model
        self.variables = variables

    def formulate_goal(self):
        return "Maximize  4x + 2y + z  subject to all constraints"

    def act(self, environment):
        print(f"Agent goal : {self.formulate_goal()}")
        return environment.solve(self.model, self.variables)

class Environment:
    def __init__(self):
        self.solver = cp_model.CpSolver()

    def get_percept(self, model, variables):
        return {
            "num_variables"  : len(variables),
            "variable_names" : list(variables.keys()),
        }

    def solve(self, model, variables):
        percept = self.get_percept(model, variables)
        print(f"Percept    : {percept['num_variables']} variables "
              f"{percept['variable_names']}")
        status = self.solver.Solve(model)
        return status, self.solver

def run_agent(agent, environment):
    return agent.act(environment)

model = cp_model.CpModel()
x = model.new_int_var(0, 20, "x")
y = model.new_int_var(0, 20, "y")
z = model.new_int_var(0, 20, "z")
model.add(x + 2 * y + z <= 20)
model.add(3 * x + y <= 18)
model.maximize(4 * x + 2 * y + z)
variables   = {"x": x, "y": y, "z": z}
agent       = OptimizationAgent(model, variables)
environment = Environment()
print("=" * 50)
print("Task 6 — Simple Optimization Problem (OR-Tools)")
print("=" * 50)
print()
print("Model Definition:")
print("  Variables   : x, y, z")
print("  Domain      : {0, 1, ..., 20}")
print("  Constraints :")
print("    1.  x + 2y + z  ≤ 20")
print("    2.  3x + y      ≤ 18")
print("  Objective   : maximize  4x + 2y + z")
print()
print("=" * 50)
status, solver = run_agent(agent, environment)
print()
print("=" * 50)
print("Solver Result")
print("=" * 50)
if status == cp_model.OPTIMAL:
    x_val = solver.value(x)
    y_val = solver.value(y)
    z_val = solver.value(z)
    obj   = solver.objective_value
    print(f"  Status         : OPTIMAL")
    print()
    print(f"  x = {x_val}")
    print(f"  y = {y_val}")
    print(f"  z = {z_val}")
    print()
    print(f"  Optimal value  : 4({x_val}) + 2({y_val}) + {z_val} = {int(obj)}")
    print()
    print("  Constraint verification:")
    lhs1 = x_val + 2 * y_val + z_val
    lhs2 = 3 * x_val + y_val
    print(f"    x + 2y + z  ≤ 20  →  {x_val} + 2({y_val}) + {z_val} = {lhs1} ≤ 20  "
          f"→  {'✓ satisfied' if lhs1 <= 20 else '✗ violated'}")
    print(f"    3x + y      ≤ 18  →  3({x_val}) + {y_val} = {lhs2} ≤ 18  "
          f"→  {'✓ satisfied' if lhs2 <= 18 else '✗ violated'}")
    print()
    print(f"  Solver wall time : {solver.wall_time:.6f} s")
    print(f"  Branches explored: {solver.num_branches}")
elif status == cp_model.FEASIBLE:
    print("  Status : FEASIBLE (not proven optimal)")
    print(f"  Objective value : {int(solver.objective_value)}")
else:
    print("  Status : NO SOLUTION / INFEASIBLE")
    print("  The constraints cannot be satisfied over the given domain.")
