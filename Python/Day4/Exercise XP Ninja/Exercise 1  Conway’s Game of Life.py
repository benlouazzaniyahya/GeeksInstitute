import time
import copy

# ===============================
# Game of Life Class
# ===============================
class GameOfLife:
    def __init__(self, rows, cols, initial_state=None):
        self.rows = rows
        self.cols = cols

        # Initialize grid with dead cells
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

        # If initial state is given, set alive cells
        if initial_state:
            for (r, c) in initial_state:
                if 0 <= r < rows and 0 <= c < cols:
                    self.grid[r][c] = 1

    def display_grid(self):
        for row in self.grid:
            print(" ".join("■" if cell else " " for cell in row))
        print("\n" + "-" * (self.cols * 2))

    def count_live_neighbors(self, row, col):
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        count = 0
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols:
                count += self.grid[r][c]
        return count

    def next_generation(self):
        new_grid = copy.deepcopy(self.grid)

        for r in range(self.rows):
            for c in range(self.cols):
                live_neighbors = self.count_live_neighbors(r, c)

                if self.grid[r][c] == 1:  # Alive
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_grid[r][c] = 0
                else:  # Dead
                    if live_neighbors == 3:
                        new_grid[r][c] = 1

        self.grid = new_grid


# ===============================
# Main Game Loop
# ===============================
if __name__ == "__main__":
    # Example: Glider Pattern
    initial_state = [
        (1, 2), (2, 3), (3, 1), (3, 2), (3, 3)
    ]

    game = GameOfLife(rows=10, cols=10, initial_state=initial_state)

    generations = 10
    for gen in range(generations):
        print(f"Generation {gen + 1}:")
        game.display_grid()
        game.next_generation()
        time.sleep(0.5)  # Delay for animation effect
