class VacuumCleaner:
    def __init__(self, environment):
        self.environment = environment
        self.rows = len(environment)
        self.cols = len(environment[0])
        self.current_row = 0
        self.current_col = 0

    def clean(self):
        while True:
            print("Current Environment:")
            self.display_environment()
            dirty_row, dirty_col = self.find_dirty_square()
            if dirty_row is None:
                print("All squares are clean.")
                break
            print(f"Moving to clean square at ({dirty_row}, {dirty_col})")
            self.move_to_square(dirty_row, dirty_col)
            print(f"Cleaning square at ({dirty_row}, {dirty_col})")
            self.environment[dirty_row][dirty_col] = 0

    def find_dirty_square(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.environment[row][col] == 1:
                    return row, col
        return None, None

    def move_to_square(self, target_row, target_col):
        while self.current_row != target_row or self.current_col != target_col:
            if self.current_row < target_row:
                self.move_down()
            elif self.current_row > target_row:
                self.move_up()
            elif self.current_col < target_col:
                self.move_right()
            elif self.current_col > target_col:
                self.move_left()

    def move_up(self):
        if self.current_row > 0:
            self.current_row -= 1

    def move_down(self):
        if self.current_row < self.rows - 1:
            self.current_row += 1

    def move_left(self):
        if self.current_col > 0:
            self.current_col -= 1

    def move_right(self):
        if self.current_col < self.cols - 1:
            self.current_col += 1

    def display_environment(self):
        for row in self.environment:
            print(row)

# Example usage:
environment = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 1, 0]
]

vacuum_cleaner = VacuumCleaner(environment)
vacuum_cleaner.clean()
