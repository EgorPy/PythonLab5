import pytest
from SmartHome import Device, Light


def test_device_has_id_and_name(lamp):
    assert lamp.id == "L1"
    assert lamp.name == "Лампа в гостиной"


def test_device_turn_on_off(lamp):
    lamp.turn_on()
    status = lamp.status()
    assert "on" in status.lower()

    lamp.turn_off()
    status = lamp.status()
    assert "off" in status.lower()


def test_device_status(lamp):
    lamp.turn_off()
    assert "off" in lamp.status()


def test_device_without_id():
    with pytest.raises(Exception):
        Light(name="Lamp", brightness=70)


def test_device_empty_id():
    with pytest.raises(Exception):
        Light("", "Lamp", 70)
