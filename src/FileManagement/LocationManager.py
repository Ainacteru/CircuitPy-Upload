from pathlib import Path

class LocationManager:

    
    def __init__(self):
        pass
    
    def get_config_file(self):
        CONFIG_PATH = Path(__file__).resolve().parents[2] / "config" / "locations.gross"
        # print(CONFIG_PATH)
        with open(CONFIG_PATH, 'r') as file:
            data = file.read()
            loc = []
            for line in data.splitlines():
                loc.append(line)
            return loc

    def getDeviceLocation(self):
        location = (self.get_config_file())[0]
        location = location[location.find("=") + 2: ].strip()

        print(location)

    def getWorkLocation(self):
        location = (self.get_config_file())[1]
        location = location[location.find("=") + 2: ].strip()

        print(location)

