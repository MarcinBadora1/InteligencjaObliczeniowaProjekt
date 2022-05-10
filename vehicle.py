class vehicle:
    """Class describing vehicle in motion!"""
    Title = "Vehicle"

Current_capacity = 1
Capacity_left = 0
localisation = 1
target_localisation = 1
    def __init__(self, current_capacity, capacity_left, localisation, target):
       self.Current_capacity = current_capacity