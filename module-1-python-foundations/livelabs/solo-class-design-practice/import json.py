import json

DATA_FILE = "Community_sharing_tools.json"

with open(DATA_File) as f:
    stations = json.load

class Tools:
    def __init__(self,Tool_name, Date, Available_tools, Tools_in_use, Safety_check):
        self.Tool_name = Tool_name
        self.Date = Date
        self.Available_tools = Available_tools
        self.Tools_in_use = Tools_in_use
        self.Safety_check = Safety_check
    def Availability_check(self):
        if self.Available_tools == 0:
            return "No Available tools at the moment, out of stock."
        else:
            return "Yes, we have some available tools for you."
    def Safety_checked(self):
        if self.Safety_check == True:
            return "Your good to go."
        else:
            return "No we can't give you the tools yet we need to a safety check."
    def __str__(self):
        return f"{self.Tool_name}: {self.}"