def test_admin_can_control_all_devices(home_with_devices, admin):
    home_with_devices.control_device(admin, "L1", "turn_on")
    home_with_devices.control_device(admin, "T1", "set_temperature", value=25)
    home_with_devices.control_device(admin, "C1", "turn_on")
    home_with_devices.control_device(admin, "V1", "turn_on")


def test_admin_can_remove_devices(home_with_devices, admin, lamp):
    home_with_devices.remove_device("L1", admin)
    assert "L1" not in home_with_devices._devices


def test_resident_can_control_lights(home_with_devices, resident):
    home_with_devices.control_device(resident, "L1", "turn_on")
    home_with_devices.control_device(resident, "L1", "set_brightness", value=80)


def test_resident_can_control_thermostat(home_with_devices, resident):
    home_with_devices.control_device(resident, "T1", "set_temperature", value=25)
    home_with_devices.control_device(resident, "T1", "turn_on")


def test_resident_can_control_vacuum_robot(home_with_devices, resident):
    home_with_devices.control_device(resident, "V1", "turn_on")


def test_resident_cannot_control_camera(home_with_devices, resident):
    home_with_devices.control_device(resident, "C1", "turn_on")


def test_resident_cannot_remove_devices(home_with_devices, resident):
    initial_count = len(home_with_devices._devices)
    home_with_devices.remove_device("L1", resident)
    assert len(home_with_devices._devices) == initial_count


def test_guest_can_control_lights(home_with_devices, guest):
    home_with_devices.control_device(guest, "L1", "turn_on")
    home_with_devices.control_device(guest, "L1", "turn_off")


def test_guest_cannot_change_light_brightness(home_with_devices, guest):
    home_with_devices.control_device(guest, "L1", "set_brightness", value=80)


def test_guest_cannot_control_thermostat(home_with_devices, guest):
    home_with_devices.control_device(guest, "T1", "set_temperature", value=28)


def test_guest_cannot_control_camera(home_with_devices, guest):
    home_with_devices.control_device(guest, "C1", "turn_on")


def test_guest_cannot_control_vacuum_robot(home_with_devices, guest):
    home_with_devices.control_device(guest, "V1", "turn_on")


def test_guest_cannot_remove_devices(home_with_devices, guest):
    initial_count = len(home_with_devices._devices)
    home_with_devices.remove_device("L1", guest)
    assert len(home_with_devices._devices) == initial_count
