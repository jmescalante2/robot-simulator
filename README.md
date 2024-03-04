python3 -m venv $VENV_PATH
$VENV_PATH/bin/pip install -U pip setuptools
$VENV_PATH/bin/pip install poetry

poetry install

if given more time
1. I will leverage containers to enhance the application's isolation, portability, and replicability
2. I will enable the users to specify the dimension of the table
3. I will extend the dimension to 3D
4. Use the built-in logger module for logging and reporting
5. Undo/Redo Functionality
6. CI/CD pipeline especially when the project becomes big

