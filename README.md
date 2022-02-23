# MarsRover

## Getting Started
1. `docker build --tag wise-robot-test .`
2. `docker run --rm -it wise-robot-test`
3. When prompted, enter the grid size in `x y` format
4. When prompted, enter the number of robots as an integer
5. When prompted, enter the initial state and commands of the robots in `(x, y, orientation) COMMANDS` format
    - You will be prompted multiple times to enter robot details if you entered a number of robots larger than 1 in step 4
