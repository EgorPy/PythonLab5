""" Fixtures """

import pytest
from SmartHome import SmartHome, Light, Thermostat, User, Camera, Role, VacuumRobot


@pytest.fixture
def home():
    return SmartHome()


@pytest.fixture
def admin():
    return User("admin", Role.ADMIN)


@pytest.fixture
def resident():
    return User("resident", Role.RESIDENT)


@pytest.fixture
def guest():
    return User("guest", Role.GUEST)


@pytest.fixture
def lamp():
    return Light("L1", "Лампа в гостиной", brightness=50)


@pytest.fixture
def thermostat():
    return Thermostat("T1", "Термостат в спальне", current=21.0)


@pytest.fixture
def camera():
    return Camera("C1", "Камера на террасе")


@pytest.fixture
def vacuum_robot():
    return VacuumRobot("R1", "Vacuum Robot")


@pytest.fixture
def home_devices(home, lamp, thermostat, camera, vacuum_robot):
    home.add_device(lamp)
    home.add_device(thermostat)
    home.add_device(camera)
    home.add_device(vacuum_robot)
    return home
