import uuid
from datetime import datetime
from pathlib import Path

from robot_simulator.command_processor import CommandProcessor
from robot_simulator.definitions import REPORT_DIRECTORY, SAMPLE_DIRECTORY
from robot_simulator.robot import Robot


def main():
    # Path to your commands file
    test_input_commands_path = Path.joinpath(
        SAMPLE_DIRECTORY, "test_input_commands.txt"
    )

    # Construct the file name
    now = datetime.now()
    report_file_name = f"robot-report-{now.strftime("%Y-%m-%d")}-{now.strftime("%H-%M-%S")}-{uuid.uuid4()}.txt"
    report_file_path = Path.joinpath(REPORT_DIRECTORY, report_file_name)

    robot = Robot(verbose=True, report_file=report_file_path)
    processor = CommandProcessor(robot)
    processor.execute_from_file(test_input_commands_path)


if __name__ == "__main__":
    main()
