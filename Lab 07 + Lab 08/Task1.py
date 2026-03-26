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
            return environment.compute_minimax(node, self.depth)

class Environment:
    def __init__(self, tree):
        self.tree = tree
        self.visit_order = []  

    def get_percept(self, node):
        return node

    def compute_minimax(self, node, depth, maximizing_player=True):
        if depth == 0 or not node.children:
            self.visit_order.append(node.value)
            node.minmax_value = node.value
            return node.value
        if maximizing_player:
            value = -math.inf
            for child in node.children:
                child_value = self.compute_minimax(child, depth - 1, False)
                value = max(value, child_value)
            node.minmax_value = value
            self.visit_order.append(node.value)
            return value
        else:
            value = math.inf
            for child in node.children:
                child_value = self.compute_minimax(child, depth - 1, True)
                value = min(value, child_value)
            node.minmax_value = value
            self.visit_order.append(node.value)
            return value

def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    result = agent.act(percept, environment)
    return result


root = Node('Root')
n1   = Node('N1')
n2   = Node('N2')
n3   = Node('N3')
n4   = Node('N4')
n5   = Node('N5')
n6   = Node('N6')
leaf_4  = Node(4)
leaf_7  = Node(7)
leaf_2  = Node(2)
leaf_5  = Node(5)
leaf_1  = Node(1)
leaf_8  = Node(8)
leaf_3  = Node(3)
leaf_6  = Node(6)
root.children = [n1, n2]
n1.children   = [n3, n4]
n2.children   = [n5, n6]
n3.children   = [leaf_4, leaf_7]
n4.children   = [leaf_2, leaf_5]
n5.children   = [leaf_1, leaf_8]
n6.children   = [leaf_3, leaf_6]
print("=" * 50)
print("TASK 1A: Full Minimax (depth = 3)")
print("=" * 50)
depth = 3
agent       = MinimaxAgent(depth)
environment = Environment(root)
run_agent(agent, environment, root)
print("Visit order:", environment.visit_order)
print()
print("Minimax values for all nodes:")
print(f"  Root : {root.minmax_value}")
print(f"  N1   : {n1.minmax_value}")
print(f"  N2   : {n2.minmax_value}")
print(f"  N3   : {n3.minmax_value}")
print(f"  N4   : {n4.minmax_value}")
print(f"  N5   : {n5.minmax_value}")
print(f"  N6   : {n6.minmax_value}")
def reset_tree(nodes):
    for n in nodes:
        n.minmax_value = None
n3.value = 7   
n4.value = 5   
n5.value = 8   
n6.value = 6   
all_nodes = [root, n1, n2, n3, n4, n5, n6,
             leaf_4, leaf_7, leaf_2, leaf_5,
             leaf_1, leaf_8, leaf_3, leaf_6]
reset_tree(all_nodes)
print()
print("=" * 50)
print("TASK 1B: Depth-limited Minimax (depth = 2)")
print("=" * 50)
depth_limited = 2
agent_dl       = MinimaxAgent(depth_limited)
environment_dl = Environment(root)
run_agent(agent_dl, environment_dl, root)
print("Visit order:", environment_dl.visit_order)
print()
print("Minimax values with depth limit = 2:")
print(f"  Root : {root.minmax_value}")
print(f"  N1   : {n1.minmax_value}")
print(f"  N2   : {n2.minmax_value}")
print(f"  N3   : {n3.minmax_value}  ← heuristic value (leaf at depth limit)")
print(f"  N4   : {n4.minmax_value}  ← heuristic value (leaf at depth limit)")
print(f"  N5   : {n5.minmax_value}  ← heuristic value (leaf at depth limit)")
print(f"  N6   : {n6.minmax_value}  ← heuristic value (leaf at depth limit)")
print()
print("Note: at depth = 2 the search stops at N3–N6; their .value")
print("acts as a heuristic evaluation score (no deeper expansion).")
