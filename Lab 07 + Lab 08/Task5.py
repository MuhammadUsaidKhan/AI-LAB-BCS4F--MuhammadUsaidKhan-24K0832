!pip install ortools
from ortools.sat.python import cp_model

class SolutionPrinter(cp_model.CpSolverSolutionCallback):
    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.variables      = variables   
        self.solution_count = 0
        self.all_solutions  = []         

    def on_solution_callback(self):
        """Automatically invoked by the solver each time a solution is found."""
        self.solution_count += 1
        solution = {name: self.value(var)
                    for name, var in self.variables.items()}
        self.all_solutions.append(solution)
        a, b, c = solution["A"], solution["B"], solution["C"]
        print(f"  Solution {self.solution_count:>2} :  A={a}  B={b}  C={c}")

class CSPAgent:
    def __init__(self, model, variables):
        self.model     = model
        self.variables = variables

    def formulate_goal(self):
        return "Enumerate ALL valid assignments of A, B, C"

    def act(self, environment):
        print(f"Agent goal : {self.formulate_goal()}")
        return environment.solve_all(self.model, self.variables)

class Environment:
    def __init__(self):
        self.solver = cp_model.CpSolver()

    def get_percept(self, model, variables):
        return {
            "num_variables"  : len(variables),
            "variable_names" : list(variables.keys()),
        }

    def solve_all(self, model, variables):
        percept = self.get_percept(model, variables)
        print(f"Percept    : {percept['num_variables']} variables "
              f"{percept['variable_names']}")
        self.solver.parameters.enumerate_all_solutions = True
        callback = SolutionPrinter(variables)
        status   = self.solver.Solve(model, callback)
        return status, self.solver, callback

def run_agent(agent, environment):
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
print("=" * 50)
print("Task 5 — All Possible Solutions (OR-Tools)")
print("=" * 50)
print()
print("CSP Definition:")
print("  Variables   : A, B, C")
print("  Domain      : {0, 1, 2, 3}")
print("  Constraints : A ≠ B  |  B ≠ C  |  A + B ≤ 4")
print()
print("=" * 50)
status, solver, callback = run_agent(agent, environment)
print()
print("=" * 50)
print("Summary")
print("=" * 50)
if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print(f"  Total solutions found : {callback.solution_count}")
    print(f"  Solver wall time      : {solver.wall_time:.6f} s")
    print()
    print("  Verification — all constraints checked per solution:")
    print(f"  {'#':>3}  {'A':>2}  {'B':>2}  {'C':>2}  "
          f"{'A≠B':>5}  {'B≠C':>5}  {'A+B≤4':>7}")
    print("  " + "-" * 43)
    for i, sol in enumerate(callback.all_solutions, 1):
        a, b, c = sol["A"], sol["B"], sol["C"]
        ok1 = "✓" if a != b       else "✗"
        ok2 = "✓" if b != c       else "✗"
        ok3 = "✓" if a + b <= 4   else "✗"
        print(f"  {i:>3}  {a:>2}  {b:>2}  {c:>2}  "
              f"{ok1:>5}  {ok2:>5}  {ok3:>7}")
else:
    print("  Status : NO SOLUTION EXISTS")
    print("  The constraints cannot be satisfied over domain {0, 1, 2, 3}.")
