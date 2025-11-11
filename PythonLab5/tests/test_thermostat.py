import pytest


def test_thermostat_current_temperature(thermostat):
    status = thermostat.status()
    assert "21.0" in status


def test_thermostat_target_temperature_set_get(thermostat):
    thermostat.target = 25
    assert thermostat.target == 25

    status = thermostat.status()
    assert "25" in status


def test_thermostat_turn_on_off(thermostat):
    thermostat.turn_on()
    status = thermostat.status()
    assert "on" in status.lower() or "включён" in status.lower()

    thermostat.turn_off()
    status = thermostat.status()
    assert "off" in status.lower() or "выключен" in status.lower()


@pytest.mark.parametrize("bad_val", [4, 31, -10, 50])
def test_thermostat_invalid_temperature_raises(thermostat, bad_val):
    with pytest.raises(ValueError):
        thermostat.target = bad_val


@pytest.mark.parametrize("good_val", [5, 15, 22, 30])
def test_thermostat_valid_temperatures(thermostat, good_val):
    thermostat.target = good_val
    assert thermostat.target == good_val
