import self as self


class storage:
    """Class describing storage properties"""


Title = "Storage"
position = [0, 1]
storage_pickup = 1
storage_delivere = 2


def __init__(self, location, storage_pickup, storage_delivere):
    self.position = location
    self.storage_pickup = storage_pickup
    self.storage_delivere = storage_delivere


def getter_position():
    return self.position


def getter_storage_pickuped():
    return self.storage_pickup


def getter_storage_delivered():
    return self.storage_delivered
