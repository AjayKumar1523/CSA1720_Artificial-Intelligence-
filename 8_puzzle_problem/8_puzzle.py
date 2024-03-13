import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = self.calculate_cost()

    def __lt__(self, other):
        return self.cost < other.cost

    def calculate_cost(self):
        cost = self.depth
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    row = (self.state[i][j] - 1) // 3
                    col = (self.state[i][j] - 1) % 3
                    cost += abs(i - row) + abs(j - col)
        return cost

    def get_successors(self):
        successors = []
        zero_row, zero_col = self.find_zero()
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in moves:
            new_row, new_col = zero_row + dr, zero_col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = [list(row) for row in self.state]
                new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]
                successors.append(PuzzleNode(new_state, self, (dr, dc), self.depth + 1))
        return successors

    def find_zero(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def get_path(self):
        path = []
        node = self
        while node:
            path.append(node)
            node = node.parent
        return reversed(path)

def solve_8_puzzle(initial_state):
    initial_node = PuzzleNode(initial_state)
    frontier = [initial_node]
    explored = set()
    goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    while frontier:
        node = heapq.heappop(frontier)
        if node.state == goal_state:
            return node.get_path()
        
        explored.add(tuple(map(tuple, node.state)))

        for successor in node.get_successors():
            if tuple(map(tuple, successor.state)) not in explored:
                heapq.heappush(frontier, successor)

    return None

def print_solution(path):
    for i, node in enumerate(path):
        print("Step:", i)
        for row in node.state:
            print(row)
        print()

def get_user_input():
    print("Enter the initial state of the 8-puzzle (3x3 grid, use 0 to represent the empty space):")
    initial_state = []
    for i in range(3):
        row = input(f"Enter row {i + 1}: ").split()
        row = [int(num) for num in row]
        if len(row) != 3:
            print("Invalid input. Please enter 3 numbers separated by space.")
            return get_user_input()
        initial_state.append(row)
    return initial_state

initial_state = get_user_input()

solution_path = solve_8_puzzle(initial_state)
if solution_path:
    print("Solution found!")
    print_solution(solution_path)
else:
    print("No solution found.")
