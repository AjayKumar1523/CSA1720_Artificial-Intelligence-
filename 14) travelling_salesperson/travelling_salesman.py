from sys import maxsize
from itertools import permutations

def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer.")

def travellingSalesmanProblem(graph, s):
    V = len(graph)
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:
        current_pathweight = 0
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
            print(f"Traversing from {k} to {j}. Current path weight: {current_pathweight}")
        current_pathweight += graph[k][s]
        print(f"Traversing from {k} to {s}. Current path weight: {current_pathweight}")
        min_path = min(min_path, current_pathweight)
        print(f"Minimum path weight so far: {min_path}\n")
    return min_path

if __name__ == "_main_":
    V = get_integer_input("Enter the number of cities: ")
    graph = []
    print("Enter the distance matrix for the graph:")
    for _ in range(V):
        row = []
        for _ in range(V):
            distance = get_integer_input(f"Enter distance to city {_ + 1}: ")
            row.append(distance)
        graph.append(row)

    s = get_integer_input("Enter the starting city (1 to V): ") - 1
    print("\nStarting traversal...\n")
    print("Minimum path weight:", travellingSalesmanProblem(graph, s))
