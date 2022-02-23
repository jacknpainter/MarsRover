from dataclasses import dataclass
from enum import Enum
import re


class Orientation(Enum):
    N = 1
    E = 2
    S = 3
    W = 4

    def get_next(self):
        v = self.value + 1
        return Orientation(v)

    def get_prev(self):
        v = self.value - 1
        return Orientation(v)


class MovementCommand(Enum):
    F = 1
    L = 2
    R = 3


@dataclass
class Grid:
    sizex: int
    sizey: int


class Robot:
    def __init__(self, x: int, y: int, orientation: Orientation, move_commands: list):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.last_valid_pos: tuple = (self.x, self.y, self.orientation.name)
        self.lost: bool = False
        self.commands: list = move_commands

    def move_command(self, command: MovementCommand, grid: Grid):
        if command == MovementCommand.F:
            if self.orientation == Orientation.N:
                self.y += 1
            elif self.orientation == Orientation.E:
                self.x += 1
            elif self.orientation == Orientation.S:
                self.y -= 1
            elif self.orientation == Orientation.W:
                self.x -= 1
        elif command == MovementCommand.L:
            if self.orientation == Orientation.N:
                self.orientation = Orientation.W
            else:
                self.orientation = self.orientation.get_prev()
        elif command == MovementCommand.R:
            if self.orientation == Orientation.W:
                self.orientation = Orientation.N
            else:
                self.orientation = self.orientation.get_next()

        if self.x < 0 or self.y < 0:
            self.lost = True
        elif self.x > grid.sizex or self.y > grid.sizey:
            self.lost = True
        else:
            self.last_valid_pos = (self.x, self.y, self.orientation.name)


class MarsRover:
    def __init__(self, grid_size: tuple):
        self.grid: Grid = Grid(grid_size[0], grid_size[1])
        self.robots = []

    def add_robot(self, x: int, y: int, orientation: Orientation, move_commands: list):
        self.robots.append(Robot(x, y, orientation, move_commands))

    def execute_move_commands(self):
        for robot in self.robots:
            print(f"{robot.last_valid_pos} -> {''.join(str(e) for e in robot.commands)} -> ", end="")
            for command in robot.commands:
                if command in MovementCommand.__members__:
                    robot.move_command(MovementCommand[command], self.grid)
                else:
                    print(f"ERROR: {command} not a valid Movement Command!")
                if robot.lost:
                    print(robot.last_valid_pos, "LOST")
                    break
            if not robot.lost:
                print(robot.last_valid_pos)


def main():
    size_str = input("Enter Grid Size (x, y): ")
    size_list = [int(n) for n in size_str.split()]
    size = tuple(size_list)
    if len(size) == 2:
        mars_rover = MarsRover(grid_size=size)
    else:
        print("Invalid Grid Size Input")
        return

    robot_count = 0
    max_robots = 0
    try:
        max_robots = int(input("Enter No. of Robots: "))
    except ValueError:
        print("Invalid Number of Robots")
        return

    while robot_count < max_robots:
        robot_str = input("Enter Robot String: ")
        robot_list = re.findall(r'\((.*?,.*?,.*?)\)', robot_str)
        robot_tuple = tuple([x.strip() for x in robot_list[0].split(',')])
        command_str = re.search(r'([A-Z])\w+', robot_str)
        command_list = list(command_str.group(0))
        try:
            robot_x = int(robot_tuple[0])
            robot_y = int(robot_tuple[1])
        except ValueError:
            print()
            print(f"Invalid Coordinate Values: {robot_tuple[0]}, {robot_tuple[1]}")
            return

        if robot_tuple[2] in Orientation.__members__:
            robot_o = Orientation[robot_tuple[2]]
        else:
            print()
            print(f"Invalid Orientation Value: {robot_tuple[2]}")
            return

        for command in command_list:
            if command not in MovementCommand.__members__:
                print(f"Invalid Command in Command List({command}): Removing...")
                command_list.remove(command)
        mars_rover.add_robot(robot_x, robot_y, robot_o, command_list)
        robot_count += 1

    mars_rover.execute_move_commands()

    print("End of Program")


if __name__ == '__main__':
    main()
