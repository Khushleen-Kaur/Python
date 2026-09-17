from abc import ABC, abstractmethod

class Room(ABC):
    def __init__(self, num, avail):
        self.room_number = num
        self.is_available = avail

    @abstractmethod
    def calculate_price(self):
        pass

    def display_info(self):
        print(f"\n-------- Room {self.room_number} --------")
        print(f"Price: {self.price}")
        print(f"Availability : {self.is_available}")

class StandardRoom(Room):
    sr = set()
    bed_price = {
        "Single Bed" : 1200,
        "Double Bed" : 1800,
        "Twin Bed" : 1900
    }
    def __init__(self, num, avail, bed):
        super().__init__(num, avail)
        self.bed_type = bed
        self.calculate_price()
        StandardRoom.sr.add(self)

    def calculate_price(self):
        self.price = StandardRoom.bed_price[self.bed_type]
        return self.price

    def display_info(self):
        super().display_info()
        print(f"Bed Type : {self.bed_type}")

s1 = StandardRoom("SR001", "Available", "Single Bed")
s2 = StandardRoom("SR002", "Available", "Double Bed")
s3 = StandardRoom("SR003", "Available", "Twin Bed")

class DeluxeRoom(Room):
    dr = set()
    bed_price = {
        "Queen Bed" : 2500,
        "King Bed" : 3200,
        "Bunk Bed" : 2000
    }
    def __init__(self, num, avail, bed, has_breakfast):
        super().__init__(num, avail)
        self.bed_type = bed
        self.has_breakfast = has_breakfast
        self.calculate_price()
        DeluxeRoom.dr.add(self)

    def calculate_price(self):
        self.price = DeluxeRoom.bed_price[self.bed_type]
        return self.price

    def display_info(self):
        super().display_info()
        print(f"Bed Type : {self.bed_type}")
        print(f"Breakfast : {self.has_breakfast}")

d1 = DeluxeRoom("DR001", "Available", "King Bed", True)
d2 = DeluxeRoom("DR002", "Available", "Queen Bed", True)
d3 = DeluxeRoom("DR003", "Available", "Bunk Bed", False)

rooms = DeluxeRoom.dr.union(StandardRoom.sr)

room_nos = set()
for room in rooms:
    room_nos.add(room.room_number)

def book_room(room_no, state):
    for r in rooms:
        if room_no == r.room_number:
            r.is_available = state

def room_details():
    print("------- Room Details --------")
    for r in rooms:
        r.display_info()

