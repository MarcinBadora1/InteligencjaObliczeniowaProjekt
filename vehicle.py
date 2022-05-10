import self


class vehicle:
    """Class describing vehicle in motion!"""
    Title = "Vehicle"


Current_capacity = 1
Capacity_left = 0
localisation = 1
target_localisation = 1


def __init__(self, current_capacity, capacity_left, localisation, target):
    assert isinstance(current_capacity, object)
    self.Current_capacity = current_capacity
    self.Capacity_left = capacity_left
    self.localisation = localisation
    self.target_localisation = target

def getter_current_capacity():
    return self.Current_capacity
def getter_capacity_left():
    return self.Capacity_left
def getter_localisation():
    return self.localisation
def getter_target_localisation():
    return self.target_localisation