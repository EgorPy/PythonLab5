def test_camera_default_state(camera):
    status = camera.status()
    assert "idle" in status.lower() or "остановила" in status.lower()


def test_camera_start_recording(camera):
    camera.turn_on()
    status = camera.status()
    assert "recording" in status.lower() or "начала" in status.lower()


def test_camera_stop_recording(camera):
    camera.turn_on()
    camera.turn_off()
    status = camera.status()
    assert "idle" in status.lower() or "остановила" in status.lower()


def test_camera_multiple_start_stop(camera):
    for _ in range(3):
        camera.turn_on()
        status_on = camera.status()
        camera.turn_off()
        status_off = camera.status()

        assert "recording" in status_on.lower() or "начала" in status_on.lower()
        assert "idle" in status_off.lower() or "остановила" in status_off.lower()
