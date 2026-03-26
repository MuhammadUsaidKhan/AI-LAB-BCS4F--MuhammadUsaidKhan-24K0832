import math

class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []
        self.minmax_value = None
        self.best_child = None          

class MinimaxAgent:
    def __init__(self, depth):
        self.depth = depth

    def formulate_goal(self, node):
        return "Goal reached" if node.minmax_value is not None else "Searching"

    def act(self, node, environment, use_alpha_beta=False):
        goal_status = self.formulate_goal(node)
        if goal_status == "Goal reached":
            return f"Minimax value for root node: {node.minmax_value}"
        if use_alpha_beta:
            return environment.alpha_beta_search(node, self.depth, -math.inf, math.inf, True)
        else:
            return environment.compute_minimax(node, self.depth, True)


class Environment:
    def __init__(self, tree):
        self.tree = tree
        self.computed_nodes = []
        self.pruned_nodes = []

    def get_percept(self, node):
        return node

    def compute_minimax(self, node, depth, maximizing_player=True):
        if depth == 0 or not node.children:
            self.computed_nodes.append(node.value)
            node.minmax_value = node.value
            return node.value
        if maximizing_player:
            value = -math.inf
            for child in node.children:
                child_value = self.compute_minimax(child, depth - 1, False)
                if child_value > value:
                    value = child_value
                    node.best_child = child
            node.minmax_value = value
            self.computed_nodes.append(node.value)
            return value
        else:
            value = math.inf
            for child in node.children:
                child_value = self.compute_minimax(child, depth - 1, True)
                if child_value < value:
                    value = child_value
                    node.best_child = child
            node.minmax_value = value
            self.computed_nodes.append(node.value)
            return value

    def alpha_beta_search(self, node, depth, alpha, beta, maximizing_player=True):
        if depth == 0 or not node.children:
            self.computed_nodes.append(node.value)
            node.minmax_value = node.value
            return node.value
        if maximizing_player:
            value = -math.inf
            for child in node.children:
                child_value = self.alpha_beta_search(child, depth - 1, alpha, beta, False)
                if child_value > value:
                    value = child_value
                    node.best_child = child
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
                if child_value < value:
                    value = child_value
                    node.best_child = child
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


def run_agent(agent, environment, start_node, use_alpha_beta=False):
    percept = environment.get_percept(start_node)
    agent.act(percept, environment, use_alpha_beta)


def get_optimal_path(root):
    """Follow best_child pointers from root to the optimal leaf."""
    path = []
    node = root
    while node is not None:
        path.append(node.value)
        node = node.best_child
    return path


def reset_tree(nodes):
    for n in nodes:
        n.minmax_value = None
        n.best_child   = None


# ══════════════════════════════════════════════════════════════════
# MODIFIED TREE — changes made from the original Task 1/2 tree:
#
#   1. Leaf values updated:
#        Original : 4  7  2  5  1  8  3  6
#        Modified : 4  7  2  5  1  8  3  6  (N3–N6 kept)
#        N6 gets a NEW third child leaf: 10
#          → N6 now has three children instead of two
#
#   2. A completely new branch N7 added under Root:
#        N7 (Min) → N8 (Max) → leaves 9, 3
#                 → N9 (Max) → leaves 6, 11   ← 11 is highest leaf
#
# Modified tree structure:
#
#                     Root / Max
#                  /       |       \
#            N1/Min      N2/Min    N7/Min   ← extra branch
#            /   \        /   \     /   \
#        N3/Max N4/Max N5/Max N6/Max N8/Max N9/Max
#         / \    / \    / \   /|\    / \    / \
#        4   7  2   5  1   8 3  6 10 9   3  6  11
#                                ^extra leaf  ^new highest
# ══════════════════════════════════════════════════════════════════

root = Node('Root')
n1 = Node('N1')
n2 = Node('N2')
n7 = Node('N7')           
root.children = [n1, n2, n7]
n3 = Node('N3')
n4 = Node('N4')
n5 = Node('N5')
n6 = Node('N6')
n1.children = [n3, n4]
n2.children = [n5, n6]
n8 = Node('N8')
n9 = Node('N9')
n7.children = [n8, n9]
n3.children = [Node(4),  Node(7)]
n4.children = [Node(2),  Node(5)]
n5.children = [Node(1),  Node(8)]
n6.children = [Node(3),  Node(6),  Node(10)]   
n8.children = [Node(9),  Node(3)]
n9.children = [Node(6),  Node(11)]              
all_nodes = [root, n1, n2, n7, n3, n4, n5, n6, n8, n9]
depth = 3   
print("=" * 60)
print("PART A: Standard Minimax — Modified Tree (depth=3)")
print("=" * 60)
reset_tree(all_nodes)
agent_mm  = MinimaxAgent(depth)
env_mm    = Environment(root)
run_agent(agent_mm, env_mm, root, use_alpha_beta=False)
print("Computed (visited) nodes :", env_mm.computed_nodes)
print()
print("Minimax values:")
print(f"  Root : {root.minmax_value}")
print(f"  N1   : {n1.minmax_value}")
print(f"  N2   : {n2.minmax_value}")
print(f"  N7   : {n7.minmax_value}  (new branch)")
print(f"  N3   : {n3.minmax_value}")
print(f"  N4   : {n4.minmax_value}")
print(f"  N5   : {n5.minmax_value}")
print(f"  N6   : {n6.minmax_value}  (now has 3 children: 3, 6, 10)")
print(f"  N8   : {n8.minmax_value}  (new)")
print(f"  N9   : {n9.minmax_value}  (new)")
print()
print("Optimal path for Max (Root → leaf):", get_optimal_path(root))
print(f"Total nodes visited: {len(env_mm.computed_nodes)}")
print()
print("=" * 60)
print("PART B: Alpha-Beta Pruning — Modified Tree (depth=3)")
print("=" * 60)
reset_tree(all_nodes)
agent_ab = MinimaxAgent(depth)
env_ab   = Environment(root)
run_agent(agent_ab, env_ab, root, use_alpha_beta=True)
print()
print("-" * 60)
print("Computed (visited) nodes :", env_ab.computed_nodes)
print("Pruned nodes             :", env_ab.pruned_nodes if env_ab.pruned_nodes else "None")
print()
print("Minimax values:")
print(f"  Root : {root.minmax_value}")
print(f"  N1   : {n1.minmax_value}")
print(f"  N2   : {n2.minmax_value}")
print(f"  N7   : {n7.minmax_value}  (new branch)")
print(f"  N3   : {n3.minmax_value}")
print(f"  N4   : {n4.minmax_value}")
print(f"  N5   : {n5.minmax_value}")
print(f"  N6   : {n6.minmax_value}  (3 children: 3, 6, 10)")
print(f"  N8   : {n8.minmax_value}  (new)")
print(f"  N9   : {n9.minmax_value}  (new)")
print()
print("Optimal path for Max (Root → leaf):", get_optimal_path(root))
print(f"Total nodes visited : {len(env_ab.computed_nodes)}")
print(f"Total nodes pruned  : {len(env_ab.pruned_nodes)}")
original_mm_count = 15     
original_ab_count = 15      
modified_mm_count = len(env_mm.computed_nodes)
modified_ab_count = len(env_ab.computed_nodes)
print()
print("=" * 60)
print("PART C: Comparison — Original vs Modified Tree")
print("=" * 60)
print(f"{'':30} {'Original':>10} {'Modified':>10}")
print(f"  {'Nodes — Standard Minimax':<28} {original_mm_count:>10} {modified_mm_count:>10}")
print(f"  {'Nodes — Alpha-Beta':<28} {original_ab_count:>10} {modified_ab_count:>10}")
print(f"  {'Nodes pruned — Alpha-Beta':<28} {'0':>10} {len(env_ab.pruned_nodes):>10}")
print(f"  {'Root minimax value':<28} {'6':>10} {root.minmax_value:>10}")

print("""
1. Root value change
   The original root value was 6. With the new N7 branch (N8→max(9,3)=9,
   N9→max(6,11)=11, N7→min(9,11)=9), N7 returns 9 to Root. However Root
   (Max) still picks the best among N1=5, N2=6, N7=9 → root becomes 9.
   The new branch raises the root value because it offers Max a better
   guaranteed outcome than either original subtree.

2. Extra leaf on N6 (value 10)
   N6 now evaluates to max(3, 6, 10) = 10 instead of 6. However N2 (Min)
   takes min(N5=8, N6=10) = 8, which is worse for N2 than the original
   min(8,6)=6. This actually hurts Max at the root because N2 used to
   contribute 6 but now contributes 8 — yet Root still prefers N7=9.

3. Pruning behaviour
   No pruning occurs in either the original or the modified tree. This is
   because the leaf ordering never causes Min's beta to drop below Max's
   alpha before all children are explored. Pruning is order-dependent: it
   fires most effectively when the best moves appear first (descending for
   Max nodes, ascending for Min nodes). With the current leaf arrangement,
   Min nodes always finish evaluating all children before the cutoff
   condition beta <= alpha is satisfied, so no branches are skipped.

4. Optimal path
   The optimal path now goes through the new N7 branch rather than the
   original N2 subtree, reflecting that the newly added leaves 9 and 11
   give Max a better guarantee at the root.
""")
