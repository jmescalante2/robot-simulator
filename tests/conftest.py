import pytest

from robot_simulator.robot import Robot
from robot_simulator.table import Table


@pytest.fixture
def standard_table():
    return Table(5, 5)
