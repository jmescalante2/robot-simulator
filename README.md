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
python3 -m venv .venv
source venv/bin/activate
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
1. Go to the samples folder and check or modify the contents test_input_commands.txt
```bash
cd <project-root-directory>/samples
nano test_input_commands.txt
```
2. Then, run the service by executing
```bash
poetry run app
``` 
The status of each command will be displayed to the terminal and the robot's reports will be saved in a file under the <project-root-directory>/samples/reports directory

## Future Improvements
Given additional time, we could:

1. Utilize containers to enhance the script's isolation, portability, and replicability.
2. Develop a graphical user interface (GUI) for the project, making it more accessible and user-friendly for individuals without a technical background, thereby widening the project's user base and enhancing interaction
3. Allow users to specify the dimensions of the table.
4. Expand the dimensions to 3D.
5. Use the built-in logging module instead of print statements. Additionally, include more detailed messages for failures to assist developers in troubleshooting.
6. Introduce Undo/Redo functionality, providing users with the ability to revert and reapply actions.
7. Establish a CI/CD pipeline, particularly as the project scales, to streamline development processes, automate testing, and ensure reliable deployments.
8. Parameterize the script using argparse or a more advanced tool such as Pydantic for handling multiple configuration sources, enhancing usability and configurability.
 

