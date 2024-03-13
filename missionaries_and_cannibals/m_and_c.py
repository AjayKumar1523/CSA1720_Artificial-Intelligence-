class State:
    def __init__(self, missionaries, cannibals, boat):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat

    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3:
            return False
        if self.cannibals > self.missionaries > 0 or 3 - self.cannibals > 3 - self.missionaries > 0:
            return False
        return True

    def __eq__(self, other):
        return self.missionaries == other.missionaries and self.cannibals == other.cannibals and self.boat == other.boat

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

    def __str__(self):
        return f"Missionaries: {self.missionaries}, Cannibals: {self.cannibals}, Boat: {self.boat}"

def get_successors(state):
    successors = []
    if state.boat == 'left':
        successors.extend([State(state.missionaries - 1, state.cannibals, 'right'),
                           State(state.missionaries, state.cannibals - 1, 'right'),
                           State(state.missionaries - 2, state.cannibals, 'right'),
                           State(state.missionaries, state.cannibals - 2, 'right'),
                           State(state.missionaries - 1, state.cannibals - 1, 'right')])
    else:
        successors.extend([State(state.missionaries + 1, state.cannibals, 'left'),
                           State(state.missionaries, state.cannibals + 1, 'left'),
                           State(state.missionaries + 2, state.cannibals, 'left'),
                           State(state.missionaries, state.cannibals + 2, 'left'),
                           State(state.missionaries + 1, state.cannibals + 1, 'left')])
    return [succ for succ in successors if succ.is_valid()]

def dfs(state, visited):
    print(state)
    if state == State(0, 0, 'right'):
        return True

    visited.add(state)

    successors = get_successors(state)
    for succ in successors:
        if succ not in visited:
            if dfs(succ, visited):
                return True

    visited.remove(state)
    return False

def solve():
    initial_state = State(3, 3, 'left')
    visited = set()
    return dfs(initial_state, visited)

if solve():
    print("Solution exists.")
else:
    print("No solution.")
