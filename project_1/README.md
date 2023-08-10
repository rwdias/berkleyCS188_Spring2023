# Pacman AI Project

Welcome to the Pacman AI project! This project focuses on implementing various search algorithms and heuristics to guide Pacman through mazes in the most efficient way possible.

## Introduction

This project involves implementing search algorithms and heuristics for Pacman to navigate mazes and achieve different objectives.

## Project Structure

- `searchAgents.py`: Implements search agents and heuristics.
- `search.py`: Contains search algorithms like DFS, BFS, UCS, A*.
- `util.py`: Provides utility classes for data structures.
- `pacman.py`: Main game file to run Pacman simulation.
- `autograder.py`: Tests implementations against predefined cases.
- `layouts/`: Contains maze layouts for testing.
- `commands.txt`: List of project commands.

## Running the Project

To play Pacman:


```python pacman.py ```


For specific algorithms or heuristics:


```python pacman.py -l <layout> -p <AgentType> -a fn=<functionName>```


For options:

```python pacman.py -h```


## Milestones

1. **Depth First Search**: Implement DFS algorithm.
2. **Breadth First Search**: Implement BFS algorithm.
3. **Uniform-Cost Search**: Implement UCS algorithm.
4. **A* Search**: Implement A* algorithm.
5. **Finding All Corners**: Implement heuristic for corners problem.
6. **Heuristic for Eating Dots**: Design heuristic for efficient dot eating.
7. **Suboptimal Search**: Implement agent to greedily eat closest dots.

## Credits

This project is based on the Berkeley CS188 Pacman Project.

## License

This project is licensed under the MIT License.
