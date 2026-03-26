import math

class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []
        self.minmax_value = None

class MinimaxAgent:
    def __init__(self, depth):
        self.depth = depth

    def formulate_goal(self, node):
        return "Goal reached" if node.minmax_value is not None else "Searching"

    def act(self, node, environment):
        goal_status = self.formulate_goal(node)
        if goal_status == "Goal reached":
            return f"Minimax value for root node: {node.minmax_value}"
        else:
            return environment.alpha_beta_search(node, self.depth, -math.inf, math.inf, True)

class Environment:
    def __init__(self, tree):
        self.tree = tree
        self.computed_nodes = []
        self.pruned_nodes = []

    def get_percept(self, node):
        return node

    def alpha_beta_search(self, node, depth, alpha, beta, maximizing_player=True):
        if depth == 0 or not node.children:
            self.computed_nodes.append(node.value)
            node.minmax_value = node.value
            return node.value
        if maximizing_player:
            value = -math.inf
            for child in node.children:
                child_value = self.alpha_beta_search(child, depth - 1, alpha, beta, False)
                value = max(value, child_value)
                alpha = max(alpha, value)
                print(f"  [Max] Node={node.value}, child={child.value}, "
                      f"value={value}, alpha={alpha}, beta={beta}")
                if beta <= alpha:
                    siblings = node.children[node.children.index(child) + 1:]
                    for s in siblings:
                        print(f"  *** Pruned: {s.value}  (beta={beta} <= alpha={alpha}) ***")
                        self.pruned_nodes.append(s.value)
                    break
            node.minmax_value = value
            self.computed_nodes.append(node.value)
            return value
        else:
            value = math.inf
            for child in node.children:
                child_value = self.alpha_beta_search(child, depth - 1, alpha, beta, True)
                value = min(value, child_value)
                beta = min(beta, value)
                print(f"  [Min] Node={node.value}, child={child.value}, "
                      f"value={value}, alpha={alpha}, beta={beta}")
                if beta <= alpha:
                    siblings = node.children[node.children.index(child) + 1:]
                    for s in siblings:
                        print(f"  *** Pruned: {s.value}  (beta={beta} <= alpha={alpha}) ***")
                        self.pruned_nodes.append(s.value)
                    break
            node.minmax_value = value
            self.computed_nodes.append(node.value)
            return value

def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    agent.act(percept, environment)

root = Node('Root')
n1   = Node('N1')
n2   = Node('N2')
root.children = [n1, n2]
n3 = Node('N3')
n4 = Node('N4')
n5 = Node('N5')
n6 = Node('N6')
n1.children = [n3, n4]
n2.children = [n5, n6]
n3.children = [Node(4), Node(7)]
n4.children = [Node(2), Node(5)]
n5.children = [Node(1), Node(8)]
n6.children = [Node(3), Node(6)]
depth = 3
agent       = MinimaxAgent(depth)
environment = Environment(root)
print("=" * 58)
print("TREE 1 — Task tree  (leaves: 4 7 2 5 1 8 3 6)")
print("Alpha-Beta Pruning — step-by-step trace")
print("=" * 58)
run_agent(agent, environment, root)
print()
print("-" * 58)
print("Computed (visited) nodes :", environment.computed_nodes)
print("Pruned nodes             :", environment.pruned_nodes if environment.pruned_nodes else "None")
print()
print("Minimax values:")
print(f"  Root : {root.minmax_value}")
print(f"  N1   : {n1.minmax_value}")
print(f"  N2   : {n2.minmax_value}")
print(f"  N3   : {n3.minmax_value}")
print(f"  N4   : {n4.minmax_value}")
print(f"  N5   : {n5.minmax_value}")
print(f"  N6   : {n6.minmax_value}")
standard_count_t1 = 15
ab_count_t1       = len(environment.computed_nodes)
print()
print("Comparison (Tree 1):")
print(f"  Nodes visited — Standard Minimax : {standard_count_t1}")
print(f"  Nodes visited — Alpha-Beta        : {ab_count_t1}")
print(f"  Nodes saved by pruning            : {standard_count_t1 - ab_count_t1}")
print()
print("  Note: this leaf ordering does not trigger any cutoff,")
print("  so all 15 nodes are visited. The result is still correct.")
root2 = Node('A')
b = Node('B'); c = Node('C')
root2.children = [b, c]
d = Node('D'); e = Node('E'); f = Node('F'); g = Node('G')
b.children = [d, e]; c.children = [f, g]
d.children = [Node(2), Node(3)]
e.children = [Node(5), Node(9)]
f.children = [Node(0), Node(1)]
g.children = [Node(7), Node(5)]
agent2       = MinimaxAgent(depth)
environment2 = Environment(root2)
print()
print("=" * 58)
print("TREE 2 — Pruning demo  (leaves: 2 3 5 9 0 1 7 5)")
print("Alpha-Beta Pruning — step-by-step trace")
print("=" * 58)
run_agent(agent2, environment2, root2)
print()
print("-" * 58)
print("Computed (visited) nodes :", environment2.computed_nodes)
print("Pruned nodes             :", environment2.pruned_nodes if environment2.pruned_nodes else "None")
print()
print("Minimax values:")
print(f"  A : {root2.minmax_value}")
print(f"  B : {b.minmax_value}")
print(f"  C : {c.minmax_value}")
print(f"  D : {d.minmax_value}")
print(f"  E : {e.minmax_value}")
print(f"  F : {f.minmax_value}")
print(f"  G : {g.minmax_value}")
standard_count_t2 = 15
ab_count_t2       = len(environment2.computed_nodes)
print()
print("Comparison (Tree 2):")
print(f"  Nodes visited — Standard Minimax : {standard_count_t2}")
print(f"  Nodes visited — Alpha-Beta        : {ab_count_t2}")
print(f"  Nodes saved by pruning            : {standard_count_t2 - ab_count_t2}")
print()
print("=" * 58)
print("Why Alpha-Beta Reduces Computation")
print("=" * 58)
print("""
  Alpha-Beta maintains two running bounds during the search:
    alpha — the best (highest) score Max can already guarantee.
    beta  — the best (lowest)  score Min can already guarantee.
  Pruning condition: when beta <= alpha at any node, the current
  player would never choose this branch because the opponent
  already has a better alternative elsewhere.
  Those subtrees are cut (never expanded), saving node visits
  while producing the EXACT same result as standard Minimax.
  Best case  (perfect move ordering) : O(b^(d/2)) — depth halved.
  Worst case (reverse move ordering) : O(b^d)     — same as Minimax.
  Average case (random ordering)     : O(b^(3d/4))
  Where b = branching factor, d = search depth.
""")
