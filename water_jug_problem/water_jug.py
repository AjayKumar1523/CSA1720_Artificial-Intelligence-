from collections import deque

class State:
    def _init_(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2

    def _eq_(self, other):
        return self.jug1 == other.jug1 and self.jug2 == other.jug2

    def _hash_(self):
        return hash((self.jug1, self.jug2))

def water_jug_problem(capacity1, capacity2, target):
    initial_state = State(0, 0)
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()
        print(f"Current State: Jug1={current_state.jug1}, Jug2={current_state.jug2}")

        if current_state.jug1 == target or current_state.jug2 == target:
            print("Solution Found!")
            return path

        visited.add(current_state)

        next_states = []

        next_states.append((State(capacity1, current_state.jug2), path + [(current_state, "Fill Jug1")]))
        next_states.append((State(current_state.jug1, capacity2), path + [(current_state, "Fill Jug2")]))
        next_states.append((State(0, current_state.jug2), path + [(current_state, "Empty Jug1")]))
        next_states.append((State(current_state.jug1, 0), path + [(current_state, "Empty Jug2")]))

        pour_amount = min(current_state.jug1, capacity2 - current_state.jug2)
        next_states.append((State(current_state.jug1 - pour_amount, current_state.jug2 + pour_amount), path + [(current_state, "Pour from Jug1 to Jug2")]))

        pour_amount = min(current_state.jug2, capacity1 - current_state.jug1)
        next_states.append((State(current_state.jug1 + pour_amount, current_state.jug2 - pour_amount), path + [(current_state, "Pour from Jug2 to Jug1")]))

        for state, new_path in next_states:
            if state not in visited:
                queue.append((state, new_path))

    return None

def print_solution(path):
    if path:
        print("Steps Taken:")
        for step, action in path:
            print(f"Action: {action} -> Jug1={step.jug1}, Jug2={step.jug2}")
    else:
        print("No solution found.")

capacity_jug1 = int(input("Enter capacity of Jug 1: "))
capacity_jug2 = int(input("Enter capacity of Jug 2: "))
target_volume = int(input("Enter target volume: "))

solution_path = water_jug_problem(capacity_jug1, capacity_jug2, target_volume)
print_solution(solution_path)
