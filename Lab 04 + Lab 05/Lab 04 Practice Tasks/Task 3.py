#iddfs on graph
def dls(graph, node, goal, depth, path):
    if depth < 0:
        return False

    path.append(node)

    if node == goal:
        return True

    for neighbor in graph.get(node, []):
        if dls(graph, neighbor, goal, depth-1, path):
            return True

    path.pop()
    return False


def iddfs_graph(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"\nDepth Level: {depth}")
        path = []
        if dls(graph, start, goal, depth, path):
            print("✅ Goal Found!")
            print("Path:", path)
            return
    print("❌ Goal Not Found")

#iddfs on tree
def iddfs_tree(tree, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"\nDepth Level: {depth}")
        path = []
        if dls(tree, start, goal, depth, path):
            print("✅ Goal Found!")
            print("Path:", path)
            return
    print("❌ Goal Not Found")
