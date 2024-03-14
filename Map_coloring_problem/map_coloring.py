class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def is_consistent(self, variable, value, assignment):
        for neighbor in self.constraints.get(variable, []):
            if neighbor in assignment and assignment[neighbor] == value:
                return False
        return True

    def backtrack_search(self, assignment={}):
        if len(assignment) == len(self.variables):
            return assignment

        unassigned = [var for var in self.variables if var not in assignment]
        var = unassigned[0]

        for value in self.domains[var]:
            if self.is_consistent(var, value, assignment):
                assignment[var] = value
                result = self.backtrack_search(assignment)
                if result is not None:
                    return result
                del assignment[var]
        return None

# Example usage
variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
domains = {'WA': ['R', 'G', 'B'], 'NT': ['R', 'G', 'B'], 'SA': ['R', 'G', 'B'],
           'Q': ['R', 'G', 'B'], 'NSW': ['R', 'G', 'B'], 'V': ['R', 'G', 'B'],
           'T': ['R', 'G', 'B']}
constraints = {'WA': ['NT', 'SA'], 'NT': ['WA', 'SA', 'Q'], 'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
               'Q': ['NT', 'SA', 'NSW'], 'NSW': ['Q', 'SA', 'V'], 'V': ['SA', 'NSW', 'T'],
               'T': ['V']}

map_coloring = CSP(variables, domains, constraints)
solution = map_coloring.backtrack_search()
print("Map Coloring Solution:", solution)
