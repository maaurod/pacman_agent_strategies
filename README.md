# Pac-Man Autonomous Systems

A comprehensive implementation of AI search algorithms and multi-agent systems using the classic Pac-Man game as a testbed. This repository contains two complete projects that explore fundamental concepts in artificial intelligence, including uninformed and informed search strategies, and adversarial game-playing algorithms.

## 📋 Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Projects](#projects)
  - [Project 1: Search](#project-1-search)
  - [Project 2: Multiagent](#project-2-multiagent)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Running Tests](#running-tests)
- [Key Algorithms Implemented](#key-algorithms-implemented)
- [Project Credits](#project-credits)

## 🎯 Overview

This repository implements intelligent agents for Pac-Man that can:
- Navigate through mazes using various search algorithms
- Find optimal paths to goals
- Collect food efficiently
- Play competitively against ghost opponents
- Make decisions in adversarial environments

The projects are based on UC Berkeley's AI course materials and provide hands-on experience with core AI concepts.

## 📁 Repository Structure

```
pacman_autonomous_systems/
├── README.md                          # This file
├── search/                            # Project 1: Search algorithms
│   ├── README.md                      # Detailed project 1 documentation
│   ├── search.py                      # Search algorithm implementations ⭐
│   ├── search_agents.py               # Search-based agent implementations ⭐
│   ├── pacman.py                      # Main game driver
│   ├── game.py                        # Game logic and state management
│   ├── util.py                        # Data structures (Stack, Queue, PriorityQueue)
│   ├── layouts/                       # Maze layouts for testing
│   ├── test_cases/                    # Autograder test cases
│   └── [other support files]
│
└── multiagent/                        # Project 2: Multi-agent systems
    ├── README.md                      # Detailed project 2 documentation
    ├── multi_agents.py                # Multi-agent algorithm implementations ⭐
    ├── pacman.py                      # Main game driver (multi-agent version)
    ├── game.py                        # Game logic and state management
    ├── util.py                        # Utility functions
    ├── layouts/                       # Maze layouts for testing
    ├── test_cases/                    # Autograder test cases
    └── [other support files]

⭐ = Files containing main student implementations
```

## 🎮 Projects

### Project 1: Search

**Location**: `search/`

Implements fundamental search algorithms to help Pac-Man navigate mazes and find optimal paths.

**Implemented Algorithms**:
- **Depth-First Search (DFS)** - Explores deepest nodes first
- **Breadth-First Search (BFS)** - Explores shallowest nodes first
- **Uniform Cost Search (UCS)** - Finds least-cost paths
- **A\* Search** - Informed search using heuristics

**Key Problems Solved**:
- Finding paths to fixed locations
- Eating all dots in the maze
- Visiting all corners efficiently
- Custom heuristic design for optimization

**Main Files**:
- `search.py` - Core search algorithm implementations
- `search_agents.py` - Problem definitions and search-based agents

[📖 See detailed project 1 documentation](search/README.md)

### Project 2: Multiagent

**Location**: `multiagent/`

Implements adversarial search algorithms for Pac-Man to compete against ghost opponents.

**Implemented Algorithms**:
- **Reflex Agent** - Makes decisions based on current state evaluation
- **Minimax** - Optimal play assuming adversarial opponents
- **Alpha-Beta Pruning** - Optimized minimax with pruning
- **Expectimax** - Handles probabilistic opponent behavior

**Key Concepts**:
- Game trees and adversarial search
- State evaluation functions
- Multi-agent coordination
- Optimization through pruning

**Main Files**:
- `multi_agents.py` - Multi-agent search implementations

[📖 See detailed project 2 documentation](multiagent/README.md)

## 🚀 Installation

### Prerequisites

- Python 3.6 or higher
- Standard Python libraries (included with Python)

### Setup

1. Clone this repository:
```bash
git clone <repository-url>
cd pacman_autonomous_systems
```

2. No additional dependencies required! The projects use only Python standard library.

## 🎯 Quick Start

### Running Pac-Man with Search Algorithms

Navigate to the search directory and try different algorithms:

```bash
cd search

# Play manually (use arrow keys)
python pacman.py

# Watch DFS in action
python pacman.py -l mediumMaze -p SearchAgent

# Try BFS
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs

# Use A* with Manhattan heuristic
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattan_heuristic

# Solve corners problem
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
```

### Running Pac-Man with Multi-Agent Algorithms

Navigate to the multiagent directory:

```bash
cd multiagent

# Play manually
python pacman.py

# Watch Reflex Agent
python pacman.py -p ReflexAgent

# Run Minimax agent
python pacman.py -p MinimaxAgent -l minimaxClassic -a depth=3

# Run Alpha-Beta agent
python pacman.py -p AlphaBetaAgent -a depth=3 -l smallClassic

# Run Expectimax agent
python pacman.py -p ExpectimaxAgent -l minimaxClassic -a depth=3
```

### Useful Command Line Options

- `-l LAYOUT` - Specify maze layout (e.g., `tinyMaze`, `mediumMaze`, `bigMaze`)
- `-p AGENT` - Choose agent type
- `-a ARGS` - Pass arguments to agent (e.g., `fn=astar,heuristic=manhattan_heuristic`)
- `-z ZOOM` - Zoom level for display
- `-q` - Run without graphics (faster)
- `-n NUM` - Run NUM games
- `--frameTime TIME` - Animation speed (0 for fastest)

Run with `-h` for complete options:
```bash
python pacman.py -h
```

## 🧪 Running Tests

Both projects include autograders to test implementations:

### Search Project Tests
```bash
cd search

# Test all questions
python autograder.py

# Test specific question (e.g., Q2)
python autograder.py -q q2

# Run without graphics
python autograder.py --no-graphics
```

### Multiagent Project Tests
```bash
cd multiagent

# Test all questions
python autograder.py

# Test specific question (e.g., Q2 - Minimax)
python autograder.py -q q2

# Run specific test case
python autograder.py -t test_cases/q2/0-small-tree
```

## 🧠 Key Algorithms Implemented

### Search Algorithms (Project 1)

| Algorithm | File | Function | Description |
|-----------|------|----------|-------------|
| DFS | `search.py` | `depth_first_search()` | Graph search exploring deepest nodes first |
| BFS | `search.py` | `breadth_first_search()` | Graph search exploring shallowest nodes first |
| UCS | `search.py` | `uniform_cost_search()` | Cost-based search finding least-cost paths |
| A\* | `search.py` | `a_star_search()` | Informed search using heuristic + cost |

### Multi-Agent Algorithms (Project 2)

| Algorithm | File | Class | Description |
|-----------|------|-------|-------------|
| Reflex Agent | `multi_agents.py` | `ReflexAgent` | Simple reflex agent with evaluation function |
| Minimax | `multi_agents.py` | `MinimaxAgent` | Optimal adversarial search |
| Alpha-Beta | `multi_agents.py` | `AlphaBetaAgent` | Minimax with pruning optimization |
| Expectimax | `multi_agents.py` | `ExpectimaxAgent` | Probabilistic opponent modeling |

### Custom Search Problems (Project 1)

- **PositionSearchProblem** - Navigate to specific location
- **CornersProblem** - Visit all four corners
- **FoodSearchProblem** - Collect all food pellets
- **AnyFoodSearchProblem** - Find path to closest food

### Evaluation Functions (Project 2)

- **Reflex Evaluation** - State-action pair evaluation considering food distance and ghost proximity
- **Better Evaluation** - Advanced state evaluation for improved performance

## 🎓 Project Credits

These projects are based on the Pac-Man AI projects developed at **UC Berkeley**:
- Original projects by John DeNero and Dan Klein
- Course materials from [Berkeley CS188: Introduction to Artificial Intelligence](https://ai.berkeley.edu)
- Student-side autograding by Brad Miller, Nick Hay, and Pieter Abbeel

**License**: Free to use for educational purposes. See individual project files for detailed licensing information.

## 📚 Learning Resources

- [Berkeley AI Course](https://ai.berkeley.edu)
- [Project 1: Search](https://ai.berkeley.edu/search.html)
- [Project 2: Multiagent](https://ai.berkeley.edu/multiagent.html)

## 🤝 Contributing

This is an educational repository. Is it done for the course Autonomous Systems at UPF EMAI course.
