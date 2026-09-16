
class MetroTrain:

    def __init__(self, id, cap, stat):
        self.transport_id = id
        self.capacity = cap
        self.status = stat

    def start(self):
        ...

    def stop(self):
        pass
    
    def display_status(self):
        print(f"Status: {self.status}")