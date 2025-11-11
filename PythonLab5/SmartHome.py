from abc import ABC, abstractmethod
from enum import Enum

class Role(Enum):
    ADMIN = "admin"
    RESIDENT = "resident"
    GUEST = "guest"

class Device(ABC):
    def __init__(self, id, name):
        self._id = id
        self._name = name
        self._is_on = False

    @abstractmethod
    def turn_on(self):
        self._is_on = True

    @abstractmethod
    def turn_off(self):
        self._is_on = False

    @abstractmethod
    def status(self):
        pass

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

class Light(Device):
    def __init__(self, id, name, brightness=100):
        super().__init__(id, name)

        if len(str(id)) == 0:
            raise ValueError("Id cannot be empty")

        self._brightness = brightness

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, value):
        if 0 <= value <= 100:
            self._brightness = value
        else:
            raise ValueError("Brightness must be 0-100")

    def turn_on(self):
        self._is_on = True
        print(f"{self._name} включена на {self._brightness}% яркости")

    def turn_off(self):
        self._is_on = False
        print(f"{self._name} выключена")

    def status(self):
        return f"{self._name}: {'on' if self._is_on else 'off'}, brightness {self._brightness}%"

class Thermostat(Device):
    def __init__(self, id, name, current=20, target=22):
        super().__init__(id, name)
        self._current = current
        self._target = target

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, value):
        if 5 <= value <= 30:
            self._target = value
        else:
            raise ValueError("Temperature must be 5-30°C")

    def turn_on(self):
        self._is_on = True
        print(f"{self._name} включён, целевая температура {self._target}°C")

    def turn_off(self):
        self._is_on = False
        print(f"{self._name} выключен")

    def status(self):
        return f"{self._name}: {'on' if self._is_on else 'off'}, current {self._current}°C, target {self._target}°C"

class Camera(Device):
    def __init__(self, id, name):
        super().__init__(id, name)
        self._recording = False

    def turn_on(self):
        self._recording = True
        print(f"{self._name} начала запись")

    def turn_off(self):
        self._recording = False
        print(f"{self._name} остановила запись")

    def status(self):
        return f"{self._name}: {'recording' if self._recording else 'idle'}"

class VacuumRobot(Device):
    def __init__(self, id, name):
        super().__init__(id, name)
        self._cleaning = False

    def turn_on(self):
        self._cleaning = True
        print(f"{self._name} начал уборку")

    def turn_off(self):
        self._cleaning = False
        print(f"{self._name} остановил уборку")

    def status(self):
        return f"{self._name}: {'cleaning' if self._cleaning else 'idle'}"

class SmartHome:
    def __init__(self):
        self._devices = {}

    def add_device(self, device):
        self._devices[device.id] = device
        print(f"{device.name} добавлено в умный дом")

    def remove_device(self, device_id, user):
        if user.role != Role.ADMIN:
            print(f"{user.name} не имеет права удалять устройства")
            return
        if device_id in self._devices:
            print(f"{self._devices[device_id].name} удалено")
            del self._devices[device_id]

    def control_device(self, user, device_id, action, **kwargs):
        device = self._devices.get(device_id)
        if not device:
            print("Устройство не найдено")
            return

        if isinstance(device, Light):
            if action in ["turn_on", "turn_off"] and user.role in [Role.ADMIN, Role.RESIDENT, Role.GUEST]:
                getattr(device, action)()
            elif action == "set_brightness" and user.role in [Role.ADMIN, Role.RESIDENT]:
                device.brightness = kwargs.get("value", device.brightness)
        elif isinstance(device, Thermostat):
            if action == "set_temperature" and user.role in [Role.ADMIN, Role.RESIDENT]:
                device.target = kwargs.get("value", device.target)
            elif action in ["turn_on", "turn_off"] and user.role in [Role.ADMIN, Role.RESIDENT]:
                getattr(device, action)()
            else:
                print(f"{user.name} не имеет права управлять термостатом")
        elif isinstance(device, Camera):
            if user.role == Role.ADMIN:
                getattr(device, action)()
            else:
                print(f"{user.name} не имеет права управлять камерой")
        elif isinstance(device, VacuumRobot):
            if user.role in [Role.ADMIN, Role.RESIDENT]:
                getattr(device, action)()
            else:
                print(f"{user.name} не имеет права управлять роботом")

class User:
    def __init__(self, name, role: Role):
        self.name = name
        self.role = role

print("MIET")

# home = SmartHome()
# lamp = Light("L1", "Лампа в гостиной", brightness=70)
# thermo = Thermostat("T1", "Термостат в спальне")
# camera = Camera("C1", "Камера на улице")
# robot = VacuumRobot("V1", "Робот-пылесос")

# lamp.turn_on()
# print(lamp.status())

# home.add_device(lamp)
# home.add_device(thermo)
# home.add_device(camera)
# home.add_device(robot)

# admin = User("Аня", Role.ADMIN)
# resident = User("Борис", Role.RESIDENT)
# guest = User("Иван", Role.GUEST)

# home.control_device(admin, "L1", "turn_on")
# home.control_device(resident, "T1", "set_temperature", value=25)
# home.control_device(guest, "T1", "set_temperature", value=28)
# home.control_device(resident, "V1", "turn_on")
# home.control_device(guest, "L1", "turn_off")
