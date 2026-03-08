# Python Exercises & Mini-Games

This repository is a collection of small-scale Python projects and exercises. Most of these were developed as part of a programming courses to explore specific concepts like event-driven programming, state management, and algorithmic logic.

## Overview

The projects here focus on implementing core logic in Python. For the games, I've primarily used the `simplegui` framework (CodeSkulptor) and later ported some logic to HTML5/JavaScript for web integration.

### Projects

#### 1. Pong (Classic Arcade Implementation)
A functional recreation of the classic Pong game.
* **Key Features:** Collision physics, dynamic ball velocity, and dual-player input handling.
* **Tech:** Python, `simplegui` logic.
* **Live Demo:** [Play here](https://www.svenhartmann.com/about-me#h.8hue9septvuo)

#### 2. Memory
* **Logic:** Card shuffling, state-based matching logic, and turn counting.
* **Concepts:** Arrays, randomization, and UI feedback.
* **Live Demo:** [Play here](https://www.svenhartmann.com/about-me#h.rghk874uq44c)

#### 3. Reflex Timer
* **Focus:** Precision and event timing.
* **Challenge:** Stopping the timer at exact millisecond intervals.
* **Live Demo:** [Play here](https://www.svenhartmann.com/about-me#h.r6f9dauiamo2)

#### 4. Snake
* **Implementation:** Dynamic array for the snake body, collision detection, and food generation.
* **Live Demo:** [Play here](https://www.svenhartmann.com/about-me#h.53c044wq63h0)

#### 5. Tic Tac Toe
* **Logic:** 2D grid management and win-condition verification (rows, columns, diagonals).
* **Live Demo:** [Play here](https://www.svenhartmann.com/about-me#h.hheexydncbyi)

## Technical Notes

### Porting to the Web
Since `simplegui` is a browser-based Python implementation, I have adapted the core game loops for my personal website using a native JavaScript/Canvas approach to ensure better performance and accessibility without requiring a Python interpreter.

### Running the Code
To run the original Python files:
1. Copy the code from the `.py` files.
2. Paste it into the [CodeSkulptor.org](https://py3.codeskulptor.org/) environment.
3. Click "Run".
