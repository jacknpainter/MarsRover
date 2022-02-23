# MarsRover

This is a version of the task written in Python3.

## Getting Started
1. `docker build --tag wise-robot-test .`
2. `docker run --rm -it wise-robot-test`
3. When prompted, enter the grid size in `x y` format
4. When prompted, enter the number of robots as an integer
5. When prompted, enter the initial state and commands of the robots in `(x, y, orientation) COMMANDS` format
    - You will be prompted multiple times to enter robot details if you entered a number of robots larger than 1 in step 4

## Improvements
Given more time on this task I could improve the code by:
- Splitting the code up into more files to make the code more readable
- Making the program more cyclical i.e. allowing n number of robots to be added/removed which are able to receive commands, which can then later be modified again via something like a menu system
- Reimplementing the input code in the main function to split it up into more functions, not only to make the code more readable but also to allow for more modularity in the future if the program were to be improved
