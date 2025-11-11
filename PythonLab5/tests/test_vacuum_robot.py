def test_vacuum_robot_default_state(vacuum_robot):
    status = vacuum_robot.status()
    assert "idle" in status.lower() or "остановил" in status.lower()


def test_vacuum_robot_start_cleaning(vacuum_robot):
    vacuum_robot.turn_on()
    status = vacuum_robot.status()
    assert "cleaning" in status.lower() or "начал" in status.lower()


def test_vacuum_robot_stop_cleaning(vacuum_robot):
    vacuum_robot.turn_on()
    vacuum_robot.turn_off()
    status = vacuum_robot.status()
    assert "idle" in status.lower() or "остановил" in status.lower()


def test_vacuum_robot_multiple_operations(vacuum_robot):
    for _ in range(2):
        vacuum_robot.turn_on()
        status_on = vacuum_robot.status()
        vacuum_robot.turn_off()
        status_off = vacuum_robot.status()

        assert "cleaning" in status_on.lower() or "начал" in status_on.lower()
        assert "idle" in status_off.lower() or "остановил" in status_off.lower()
