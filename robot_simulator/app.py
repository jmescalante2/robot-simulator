from robot_simulator.command_processor import CommandProcessor
from robot_simulator.robot import Robot


def main():
    robot = Robot(verbose=True)
    processor = CommandProcessor(robot)
    commands = [
        "PLACE 0,0,NORTH",
        "MOVE",
        "REPORT",
        "PLACE 0,0,NORTH",
        "LEFT",
        "REPORT",
        "PLACE 1,2,EAST",
        "MOVE",
        "MOVE",
        "LEFT",
        "MOVE",
        "REPORT",
    ]
    for cmd in commands:
        processor.execute(cmd)


if __name__ == "__main__":
    main()
