import pytest


def test_lamp_is_off_by_default(lamp):
    assert "off" in lamp.status()


def test_lamp_status_change(lamp):
    lamp.turn_on()
    assert "on" in lamp.status()


def test_lamp_brightness_change(lamp):
    lamp.brightness = 0
    assert lamp.brightness == 0


def test_lamp_brightness_valid(lamp):
    with pytest.raises(Exception):
        lamp.brightness = -10


def test_lamp_brightness_unchange(lamp):
    b = lamp.brightness
    lamp.turn_on()
    lamp.turn_off()
    assert lamp.brightness == b
