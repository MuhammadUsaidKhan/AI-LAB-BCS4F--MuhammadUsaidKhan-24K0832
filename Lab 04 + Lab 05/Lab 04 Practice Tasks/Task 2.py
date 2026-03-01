import itertools
def tsp(dist_matrix):
    cities = list(dist_matrix.keys())
    start = cities[0]
    min_path = None
    min_cost = float('inf')
    for perm in itertools.permutations(cities[1:]):
        path = [start] + list(perm) + [start]
        cost = 0
        for i in range(len(path) - 1):
            cost += dist_matrix[path[i]][path[i+1]]
        if cost < min_cost:
            min_cost = cost
            min_path = path
    return min_path, min_cost

dist_matrix = {
    'A': {'A':0,'B':10,'C':15,'D':20},
    'B': {'A':10,'B':0,'C':35,'D':25},
    'C': {'A':15,'B':35,'C':0,'D':30},
    'D': {'A':20,'B':25,'C':30,'D':0}
}
path, cost = tsp(dist_matrix)
print("\nShortest Route:", path)
print("Minimum Cost:", cost)
