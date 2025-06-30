import random
import copy
def calculate_heuristic(positions):
    attacks = 0
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            if (positions[i][0] == positions[j][0] or 
                positions[i][1] == positions[j][1] or  
                abs(positions[i][0] - positions[j][0]) == abs(positions[i][1] - positions[j][1])):
                attacks += 1
    return attacks
def move_queens(positions):
    new_positions = copy.deepcopy(positions)
    rows = list(set([pos[0] for pos in new_positions]))
    if len(rows) < 2:
        return new_positions
    row1, row2 = random.sample(rows, 2)
    idx1 = next(i for i, pos in enumerate(new_positions) if pos[0] == row1)
    idx2 = next(i for i, pos in enumerate(new_positions) if pos[0] == row2)
    col1 = new_positions[idx1][1]
    col2 = new_positions[idx2][1]
    new_positions[idx1] = (row2, col1)
    new_positions[idx2] = (row1, col2)
    return new_positions
def print_board(positions):
    board = [['.' for _ in range(8)] for _ in range(8)]
    for row, col in positions:
        if 0 <= row < 8 and 0 <= col < 8:
            board[row][col] = 'Q'    
    print("  0 1 2 3 4 5 6 7")
    print(" +-----------------+")
    for i, row in enumerate(board):
        print(f"{i}| {' '.join(row)} |")
    print(" +-----------------+")
def select_next_best_from_candidates(current_h, candidates):    
    better = [c for c in candidates if c[1] < current_h]
    if better:
        return min(better, key=lambda x: x[1])
    closest = min(candidates, key=lambda x: abs(x[1] - current_h))
    return closest
def eight_queens(initial_positions, max_step=4, max_iterations=100):
    if len(initial_positions) != 8:
        raise ValueError("Must provide exactly 8 queen positions")    
    positions = initial_positions
    stage_log = []
    step_count = 0
    iterations = 0
    current_h = calculate_heuristic(positions)    
    print(f"Step 1 (initial position)")
    print(f"Heuristic: {current_h}")
    print(f"Step count: {step_count}")
    print_board(positions)
    print()
    current_best_positions = positions
    current_best_h = current_h
    while iterations < max_iterations:
        iterations += 1
        candidates = []
        for s in range(max_step):
            new_positions = move_queens(current_best_positions)
            new_h = calculate_heuristic(new_positions)
            print(f"Step {iterations}.{s+1}")
            print(f"Heuristic: {new_h}")
            print_board(new_positions)
            print()
            candidates.append((new_positions, new_h))
        best_positions, best_h = select_next_best_from_candidates(current_best_h, candidates)
        if best_h <= current_best_h:
            print(f"Selected new solution at Step {iterations} (best of {max_step} steps)")
            current_best_positions = best_positions
            current_best_h = best_h
            if best_h == 0:
                print("Solution found!")
                break
        else:
            print(f"No better candidate found. Using closest higher heuristic.")
            current_best_positions = best_positions
            current_best_h = best_h
        print(f"Selected Heuristic: {current_best_h}")
        print_board(current_best_positions)
        print()
        stage_log.append((copy.deepcopy(current_best_positions), current_best_h))
    if current_best_h > 0:
        print("Maximum iterations reached or no solution found.")
    return stage_log, current_best_positions
def main():
    print("=== 8 Queens Problem Solver ===")
    print("Enter 8 queen positions (row and column) separated by space (e.g., 0 0):")
    user_input = []
    while len(user_input) < 8:
        try:
            row, col = map(int, input(f"Queen {len(user_input)+1} (row col): ").split())
            if 0 <= row < 8 and 0 <= col < 8:
                user_input.append((row, col))
            else:
                print("Invalid input. Make sure values are between 0 and 7.")
        except ValueError:
            print("Please enter valid numbers like '2 3'.")
    print("\nInitial Board:")
    print_board(user_input)
    print(f"Initial heuristic: {calculate_heuristic(user_input)}")
    try:
        max_step = int(input("\nEnter maximum step count before fallback (default 4): ") or 4)
        max_iterations = int(input("Enter maximum number of iterations (default 100): ") or 100)
    except ValueError:
        max_step = 4
        max_iterations = 100
    print("\nSolving...\n")
    stages, final_positions = eight_queens(user_input, max_step, max_iterations)
    print("\nFinal Board:")
    print_board(final_positions)
    print(f"Final heuristic: {calculate_heuristic(final_positions)}")
if __name__ == "__main__":
    main()
