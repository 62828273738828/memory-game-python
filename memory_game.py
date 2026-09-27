import random
import time
import os

# ─── Colors for terminal ───────────────────────────────────────────────────────
RED     = "\033[91m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
BLUE    = "\033[94m"
MAGENTA = "\033[95m"
CYAN    = "\033[96m"
WHITE   = "\033[97m"
RESET   = "\033[0m"
BOLD    = "\033[1m"

# ─── Card symbols (pairs) ──────────────────────────────────────────────────────
SYMBOLS = ["🐉", "⚔️ ", "🛡️ ", "🏆", "💎", "🔥", "⚡", "🎮"]

def clear():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

def create_board(size):
    """Create and shuffle the board with pairs of symbols."""
    symbols = (SYMBOLS * 2)[:size * size]
    random.shuffle(symbols)
    board = [symbols[i * size:(i + 1) * size] for i in range(size)]
    return board

def display_board(board, revealed, size):
    """Display the current state of the board."""
    print(f"\n  {BOLD}{CYAN}=== MEMORY GAME ==={RESET}\n")
    
    # Column numbers
    header = "     "
    for col in range(size):
        header += f"  {YELLOW}{col + 1}{RESET}  "
    print(header)
    print("     " + "─────" * size)

    for row in range(size):
        row_display = f"  {YELLOW}{row + 1}{RESET}  |"
        for col in range(size):
            if revealed[row][col]:
                row_display += f" {board[row][col]} |"
            else:
                row_display += f"  {BLUE}?{RESET}  |"
        print(row_display)
        print("     " + "─────" * size)

def get_input(prompt, size):
    """Get a valid row/column input from the player."""
    while True:
        try:
            value = int(input(prompt)) - 1
            if 0 <= value < size:
                return value
            else:
                print(f"{RED}  Please enter a number between 1 and {size}.{RESET}")
        except ValueError:
            print(f"{RED}  Invalid input. Enter a number.{RESET}")

def play():
    """Main game loop."""
    clear()
    print(f"\n  {BOLD}{MAGENTA}Welcome to Memory Game!{RESET}")
    print(f"  {WHITE}Match all pairs to win.\n{RESET}")

    # Choose difficulty
    print(f"  {YELLOW}Choose difficulty:{RESET}")
    print(f"  {GREEN}1{RESET} - Easy   (2x2)")
    print(f"  {GREEN}2{RESET} - Medium (4x4)")
    print(f"  {GREEN}3{RESET} - Hard   (4x4 with timer)\n")

    while True:
        choice = input("  Your choice (1/2/3): ").strip()
        if choice in ("1", "2", "3"):
            break
        print(f"{RED}  Please enter 1, 2 or 3.{RESET}")

    if choice == "1":
        size = 2
        time_limit = None
    elif choice == "2":
        size = 4
        time_limit = None
    else:
        size = 4
        time_limit = 60  # seconds

    # Setup
    board = create_board(size)
    revealed = [[False] * size for _ in range(size)]
    matched = [[False] * size for _ in range(size)]
    moves = 0
    pairs_found = 0
    total_pairs = (size * size) // 2
    start_time = time.time()

    while pairs_found < total_pairs:
        clear()

        # Timer display
        if time_limit:
            elapsed = int(time.time() - start_time)
            remaining = time_limit - elapsed
            if remaining <= 0:
                clear()
                print(f"\n  {RED}{BOLD}⏰ Time's up! Game over!{RESET}")
                print(f"  You found {GREEN}{pairs_found}{RESET} out of {total_pairs} pairs.\n")
                return
            timer_color = RED if remaining < 10 else YELLOW if remaining < 20 else GREEN
            print(f"\n  ⏱️  Time remaining: {timer_color}{remaining}s{RESET}")

        display_board(board, revealed, size)
        print(f"\n  {WHITE}Moves: {YELLOW}{moves}{RESET}   |   "
              f"Pairs found: {GREEN}{pairs_found}/{total_pairs}{RESET}\n")

        # First card
        print(f"  {CYAN}--- First card ---{RESET}")
        row1 = get_input(f"  Row:    ", size)
        col1 = get_input(f"  Column: ", size)

        if revealed[row1][col1]:
            print(f"{RED}  Card already revealed! Choose another.{RESET}")
            time.sleep(1)
            continue

        revealed[row1][col1] = True
        clear()
        if time_limit:
            elapsed = int(time.time() - start_time)
            remaining = time_limit - elapsed
            timer_color = RED if remaining < 10 else YELLOW if remaining < 20 else GREEN
            print(f"\n  ⏱️  Time remaining: {timer_color}{remaining}s{RESET}")
        display_board(board, revealed, size)
        print(f"\n  Moves: {YELLOW}{moves}{RESET}   |   Pairs found: {GREEN}{pairs_found}/{total_pairs}{RESET}\n")

        # Second card
        print(f"  {CYAN}--- Second card ---{RESET}")
        while True:
            row2 = get_input(f"  Row:    ", size)
            col2 = get_input(f"  Column: ", size)
            if (row2, col2) == (row1, col1) or revealed[row2][col2]:
                print(f"{RED}  Choose a different hidden card.{RESET}")
            else:
                break

        revealed[row2][col2] = True
        moves += 1

        clear()
        if time_limit:
            elapsed = int(time.time() - start_time)
            remaining = time_limit - elapsed
            timer_color = RED if remaining < 10 else YELLOW if remaining < 20 else GREEN
            print(f"\n  ⏱️  Time remaining: {timer_color}{remaining}s{RESET}")
        display_board(board, revealed, size)
        print(f"\n  Moves: {YELLOW}{moves}{RESET}   |   Pairs found: {GREEN}{pairs_found}/{total_pairs}{RESET}\n")

        # Check for match
        if board[row1][col1] == board[row2][col2]:
            print(f"  {GREEN}{BOLD}✅ Match found! {board[row1][col1]}{RESET}")
            matched[row1][col1] = True
            matched[row2][col2] = True
            pairs_found += 1
            time.sleep(1.2)
        else:
            print(f"  {RED}❌ No match. Cards will be hidden again.{RESET}")
            time.sleep(1.5)
            revealed[row1][col1] = False
            revealed[row2][col2] = False

    # Victory screen
    elapsed = int(time.time() - start_time)
    clear()
    print(f"\n  {BOLD}{GREEN}🏆 Congratulations! You won! 🏆{RESET}\n")
    print(f"  {WHITE}Moves:    {YELLOW}{moves}{RESET}")
    print(f"  {WHITE}Time:     {YELLOW}{elapsed} seconds{RESET}\n")

    # Rating
    if moves <= total_pairs + 2:
        print(f"  Rating: {YELLOW}⭐⭐⭐ Perfect!{RESET}\n")
    elif moves <= total_pairs * 2:
        print(f"  Rating: {YELLOW}⭐⭐ Great!{RESET}\n")
    else:
        print(f"  Rating: {YELLOW}⭐ Good effort!{RESET}\n")

def main():
    while True:
        play()
        again = input(f"  {CYAN}Play again? (y/n): {RESET}").strip().lower()
        if again != "y":
            print(f"\n  {MAGENTA}Thanks for playing! See you next time. 👋{RESET}\n")
            break

if __name__ == "__main__":
    main()
