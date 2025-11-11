def test_add_device_to_home(home, lamp):
    home.add_device(lamp)
    assert len(home._devices) == 1
    assert "L1" in home._devices


def test_cannot_add_duplicate_device(home, lamp):
    home.add_device(lamp)
    home.add_device(lamp)
    assert len(home._devices) == 1


def test_remove_device(home, lamp, admin):
    home.add_device(lamp)
    home.remove_device("L1", admin)
    assert len(home._devices) == 0


def test_remove_nonexistent_device(home, admin):
    home.remove_device("NONEXISTENT", admin)


def test_find_device(home_devices):
    assert len(home_devices._devices) == 4
    assert "L1" in home_devices._devices
    assert "T1" in home_devices._devices
    assert "C1" in home_devices._devices
    assert "R1" in home_devices._devices
