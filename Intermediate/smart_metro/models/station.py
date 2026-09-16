
class Station:
    total_stations = 0

    def __init__(self, id, name, line, location):
        total_stations += 1
        self.station_id = id
        self.name = name
        self.line = line
        self.location = location

    @classmethod
    def show_station_count(cls):
        print(f"Total station count: {cls.total_stations}")

    def display_info(self):
        print("\n------ Station Details ------")
        print(f"Station_id : {self.station_id}")
        print(f"Name : {self.name}")
        print(f"Line : {self.line}")
        print(f"Location : {self.location}")
