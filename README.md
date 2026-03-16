# 🐍 Sneeky Boy — Snake Game

A classic Snake game built with Python's `turtle` graphics library. Eat food, grow your snake, and beat your high score!

## Features

- Smooth snake movement with keyboard controls
- Randomly spawning food
- Real-time score display
- **Persistent high score** — saved to a local file between sessions
- Play again prompt after game over
- Wall collision and self-collision detection

## How to Play

| Key | Action |
|-----|--------|
| ↑ | Move up |
| ↓ | Move down |
| ← | Move left |
| → | Move right |

- Eat the red food to grow and earn points
- Avoid hitting the walls or your own body
- Your high score is automatically saved when you beat it

## Project Structure

```
SnakeGame/
├── main.py          # Game loop and screen setup
├── snake.py         # Snake movement, controls, and collision logic
├── food.py          # Food spawning logic
├── scoreboard.py    # Score tracking and high score persistence
└── high_score.txt   # Stores the all-time high score
```

## Getting Started

### Prerequisites

- Python 3.x (no external libraries needed — `turtle` is part of the standard library)

### Run the game

```bash
git clone https://github.com/your-username/SnakeGame.git
cd SnakeGame
python main.py
```

## How It Works

The game is built using OOP principles — each component is its own class:

- `Snake` manages the body segments, movement, and direction changes
- `Food` randomly repositions itself on the screen when eaten
- `Scoreboard` tracks the current score and reads/writes the high score from `high_score.txt`

## License

This project is open source and available under the [MIT License](LICENSE).
