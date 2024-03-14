import heapq

class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def heuristic(state, goal_state):
    return abs(state[0] - goal_state[0]) + abs(state[1] - goal_state[1])

def get_successors(state):
    successors = []
    x, y = state
    possible_moves = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    for move in possible_moves:
        if 0 <= move[0] < 3 and 0 <= move[1] < 3:  
            successors.append(move)
    return successors

def a_star(initial_state, goal_state):
    frontier = []
    heapq.heappush(frontier, Node(initial_state, None, 0, heuristic(initial_state, goal_state)))
    explored = set()

    while frontier:
        node = heapq.heappop(frontier)
        if node.state == goal_state:
            path = []
            while node:
                path.append(node.state)
                node = node.parent
            return path[::-1]  
        
        explored.add(node.state)

        for successor in get_successors(node.state):
            if successor not in explored:
                cost = node.cost + 1 
                heapq.heappush(frontier, Node(successor, node, cost, heuristic(successor, goal_state)))

    return None 

initial_state = (0, 0)
goal_state = (2, 2)
path = a_star(initial_state, goal_state)
if path:
    print("Path found:", path)
else:
    print("No path found.")
