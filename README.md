# 🟡 Pac-Man in Maze World
This repository contains my solution for COL106 Assignment 1 at IIT Delhi, which involves implementing a navigation system for Pac-Man using a 2D grid maze and stack-based pathfinding. The objective is to guide Pac-Man to his destination while avoiding ghosts, using only stacks for traversal logic.

## 🧩 Problem Statement
Pac-Man is trapped in a haunted maze modeled as a 2D grid. Some cells are occupied by ghosts (1) and cannot be traversed, while the rest are free (0). Given a start and end cell, the goal is to determine a valid path using only stacks—without recursion or built-in pathfinding libraries.
The code is structured to meet the following requirements:

- Add and remove ghosts from the maze.

- Search for a valid path avoiding ghosts.

- Use stacks (implemented from scratch) for all traversal logic.
## 🧠 Key Concepts
- Stack-based DFS traversal to explore the grid.

- Custom stack implementation (no use of Python's built-in list methods like append and pop in Navigator).

- Path validation to ensure no ghost cells are entered.

- Exception handling for invalid paths.

## 📁 Project Structure
> grid.py           # Contains the Maze class implementation
> 
> stack.py          # Custom Stack class using dynamic arrays
> 
> navigator.py      # Pathfinding logic using stack-based DFS
> 
> exception.py      # Custom exception class: PathNotFoundException
> 
> main.py           # Script to test and run the implementation
