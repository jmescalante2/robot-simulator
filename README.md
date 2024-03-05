# Robot Simulator

This project simulates a programmable robot that can navigate on a table based on textual commands. It supports basic commands for movement, rotation, placement, and status reporting. The simulator is implemented in Python and uses Poetry for dependency management.

## System Requirements

- **Python Version:** ~=3.12.2
- **Package Manager:** ~=Poetry 1.8.2

This project has been tested On macOS 13.4 (22F66)

## Setup Instructions

### Install Python 3.12

Ensure Python 3.12 is installed on your system. If it's not, you can download it from the official Python website or use a version management tool like `pyenv`.

### Clone the Project

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/jmescalante2/robot-simulator.git
cd <project-root-directory>
```

### Install Poetry

Poetry is a tool for dependency management and packaging in Python. To install Poetry, follow the installation instructions on the [Poetry documentation page](https://python-poetry.org/docs/#installation). Make sure to activate your virtual environment first before the installation.

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -U pip setuptools
pip install poetry
```

### Install Dependencies from the Lock File
```bash
poetry install
```

### Run the Unit Tests
```bash
cd <project-root-directory>
poetry run pytest
```

## Usage
1. Go to the samples folder and check or modify the contents of test_input_commands.txt. Valid commands are:
"PLACE &lt;X&gt;, &lt;Y&gt;, &lt;DIRECTION&gt;", "MOVE", "LEFT", "RIGHT", and "REPORT" where X and Y are non-negative integers, and the DIRECTION is one of NORTH, EAST, SOUTH, WEST.

```bash
cd <project-root-directory>/samples
nano test_input_commands.txt
```
2. Then, run the service by executing
```bash
poetry run app
``` 
The status of each command will be displayed on the terminal and the robot's reports will be saved in a file under the &lt;project-root-directory&gt;/samples/reports directory

## Assumptions 
1. Only one robot can be deployed at a time. Issuing subsequent place commands will only reposition the existing robot.

## Future Improvements
Given additional time, we could:

1. Utilize containers to enhance the script's isolation, portability, and replicability.
2. Develop a graphical user interface (GUI) for the project, making it more accessible and user-friendly for individuals without a technical background.
3. Allow users to specify the length and width of the table and expand the dimensions to 3D.
4. Use the built-in logging module instead of print statements. Additionally, include more detailed messages for failures to assist developers in troubleshooting.
5. Introduce Undo/Redo functionality, providing users with the ability to revert and reapply actions.
6. Establish a CI/CD pipeline, particularly as the project scales, to streamline development processes, automate testing, and ensure reliable deployments.
7. Parameterize the script using argparse or a more advanced tool such as Pydantic for handling multiple configuration sources, enhancing usability and configurability.
8. Integrate Git hooks for an automated code formatter that adheres to PEP standards, ensuring consistent coding style across the project. This can be accomplished by using a tool like pre-commit coupled with formatters like black or autopep8. Here's a step-by-step guide.
9. Allow multiple robots to be deployed.
10. Add obstructions on the table. 
 

