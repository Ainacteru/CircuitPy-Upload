from pathlib import Path
from FileManagement.VisualSelector import VisualSelector

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
        
    def setup_config_file(self):
        CONFIG_PATH = Path(__file__).resolve().parents[2] / "config" / "locations.gross"

        if not CONFIG_PATH.exists():
            # Create the file if it doesn't exist
            # holy intellisense taking over my job
            vs = VisualSelector()
            deviceLocation = vs.select_directory("Select Device Location")
            workLocation = vs.select_directory("Select Work Location")

            with open(CONFIG_PATH, 'w') as file:
                file.write(f"Device Location = {deviceLocation} \n")
                file.write(f"Work Location = {workLocation} \n")

    def getDeviceLocation(self):
        location = (self.get_config_file())[0]
        location = location[location.find("=") + 2: ].strip()

        print(location)

    def getWorkLocation(self):
        location = (self.get_config_file())[1]
        location = location[location.find("=") + 2: ].strip()

        print(location)

