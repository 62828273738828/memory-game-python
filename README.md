# 🎮 Memory Game — Python Terminal

A classic memory card matching game built with Python, running entirely in the terminal with colors and emojis.

## 📸 Preview

```
  === MEMORY GAME ===

       1     2     3     4
     ─────────────────────────
  1  |  ?  |  ?  | 🔥  |  ?  |
     ─────────────────────────
  2  |  ?  | 💎  |  ?  |  ?  |
     ─────────────────────────
  3  |  ?  |  ?  |  ?  | 🎮  |
     ─────────────────────────
  4  | 🏆  |  ?  |  ?  |  ?  |
     ─────────────────────────

  Moves: 5   |   Pairs found: 2/8
```

## ✨ Features

- 3 difficulty levels: Easy (2x2), Medium (4x4), Hard (4x4 with timer)
- Colorful terminal interface with emojis
- Move counter and timer
- Performance rating at the end (⭐ / ⭐⭐ / ⭐⭐⭐)
- Play again option

## 🚀 How to Run

**Requirements:** Python 3.6 or higher (no external libraries needed)

```bash
# Clone the repository
git clone https://github.com/your-username/memory-game-python.git

# Navigate to the folder
cd memory-game-python

# Run the game
python memory_game.py
```

> **Windows users:** For best emoji display, use Windows Terminal or VS Code terminal.

## 🕹️ How to Play

1. Choose a difficulty level
2. Enter the **row** and **column** of the first card to reveal it
3. Enter the **row** and **column** of the second card
4. If both cards match — they stay revealed! 🎉
5. If they don't match — they flip back face down
6. Match all pairs to win!

## 📁 Project Structure

```
memory-game-python/
│
├── memory_game.py   # Main game file
└── README.md        # Project documentation
```

## 🛠️ Concepts Used

- Functions and modular code structure
- Lists and 2D arrays (matrix)
- Loops (`for`, `while`) and conditionals
- User input validation
- String formatting and ANSI color codes
- `random`, `time`, and `os` standard libraries

## 👤 Author

**Caio Mendonça Silva**  
📍 Fortaleza, Brazil  
🎮 Tech enthusiast | Video editor | Python learner

---

*Built as a portfolio project to demonstrate Python fundamentals.*
