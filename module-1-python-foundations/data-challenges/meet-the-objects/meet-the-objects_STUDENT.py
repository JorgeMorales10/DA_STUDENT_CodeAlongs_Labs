#!/usr/bin/env python3
"""Meet the Objects: see DataChallengeOverview&Steps.md for the steps."""

import json

DATA_FILE = "../data/bike_stations.json"  # edit the filepath with the data

with open(DATA_FILE) as f:
    stations = json.load(f)


# ===== Day 1 =====

# Step 1: Reproduce the Parallel-List Bug and Name the Wrong Stations
# TODO: assign `names` and `bikes` to two empty lists
# TODO: loop over `stations`; append each one's "name" to `names`
# TODO: append the same station's "bikes_available" to `bikes`
names = []
bikes = []
for station in stations:
    names.append(station["name"])
    bikes.append(station["bikes_available"])

names.pop(2)
print("stations in the file:", len(stations))
# TODO: loop over range(len(names)); print names[i], "|", bikes[i], "bikes"
for ranges in range(len(names)):
    print(names[ranges], "|", bikes[ranges], "bikes") 
# Step 1, answer 1:
#
# Step 1, answer 2:
#
# Step 1, answer 3:
#


# Step 2: Define the Station Class and Prove Two Instances Are Independent
class Station:
    def __init__(self, station_id, name, capacity, bikes_available, needs_maintenance):
        self.name = name
        self.station_id = station_id
        self.capacity = capacity
        self.bikes_available = bikes_available
        self.needs_maintenance = needs_maintenance
    def needs_restock(self):
        return self.bikes_available < self.capacity/4

    # TODO: add __init__ with name (str), capacity and bikes_available (int)
    # TODO: in __init__, assign each parameter to self.<same name>
    # TODO: add a parameter and self.<name> for each extra field you agreed
    # TODO: add needs_restock(self): True if bikes_available < capacity / 4
    pass

fleet = [] #its creating an empty list 
for s in stations:
    fleet.append(Station(s["station_id"], s["name"], s["capacity"], s["bikes_available"], s["needs_maintenance"]))
busy = fleet[1]
quiet = fleet[-1]

print("Before:",busy.needs_restock(), quiet.needs_restock())

busy.bikes_available = 0 
print("After:", busy.needs_restock(), quiet.needs_restock())
# TODO: assign `fleet` to []; loop over `stations` as `s`
# TODO: append Station(s["name"], s["capacity"], s["bikes_available"])
# TODO: assign `busy`, `quiet` to two stations with equal needs_restock()
# TODO: print both needs_restock() answers
# TODO: set busy.bikes_available to 0, then print both answers again

# Step 2, answer 1:
#
# Step 2, answer 2:
#
# Step 2, answer 3:
#
# Step 2, answer 4:
#


# ===== Day 2 =====

# Step 3: Add `__str__` and Find Out Which of Four Prints It Changes
print(fleet[0]) #this will print out the first record
print(fleet[:2])

class Station:
    def __init__(self, station_id, name, capacity, bikes_available, needs_maintenance):
        self.name = name
        self.station_id = station_id
        self.capacity = capacity
        self.bikes_available = bikes_available
        self.needs_maintenance = needs_maintenance
    def needs_restock(self):
        return self.bikes_available < self.capacity / 4
    def __str__(self): #self is the self attribute your working with
        return f"{self.name}:{self.bikes_available} of {self.capacity} bikes" # f is the string literal\
    
fleet = []
for s in stations:
    fleet.append(Station(s["station_id"], s["name"], s["capacity"], s["bikes_available"], s["needs_maintenance"]))  

busy = fleet[1]
quiet = fleet[-1]
print("Before:",busy.needs_restock(), quiet.needs_restock())
busy.bikes_available = 0 
print("After:", busy.needs_restock(), quiet.needs_restock()) 
# TODO: copy your Station class from Step 2 here
# TODO: add __str__(self) to return text like "Grand Army Plaza: 6 of 48 bikes"
# TODO: build it from self.name, self.bikes_available and self.capacity
# TODO: rebuild `fleet` from this class with the same loop as Step 2

print(fleet[0])
print(fleet[:2])

# Step 3, answer 1:
#
# Step 3, answer 2:
#


# Step 4: Add `__repr__` and Print the Van List for You and the Dispatcher

class Station:
    def __init__(self, station_id, name, capacity, bikes_available, needs_maintenance):
        self.name = name
        self.station_id = station_id
        self.capacity = capacity
        self.bikes_available = bikes_available
        self.needs_maintenance = needs_maintenance
    def needs_restock(self):
        return self.bikes_available < self.capacity / 4
    def __str__(self): #self is the self attribute your working with
        return f"{self.name}:{self.bikes_available} of {self.capacity} bikes"
    def __repr__(self):
        return f"Station('{self.name}', {self.bikes_available})"

fleet = []
for s in stations:
    fleet.append(Station(s["station_id"], s["name"], s["capacity"], s["bikes_available"], s["needs_maintenance"]))  
van_list = []
for i in fleet:
    if i.needs_restock():
        van_list.append(i)

busy = fleet[1]
quiet = fleet[-1]
print("Before:",busy.needs_restock(), quiet.needs_restock())
busy.bikes_available = 0 
print("After:", busy.needs_restock(), quiet.needs_restock()) 

# TODO: copy your Station class from Step 3 here
# TODO: add __repr__(self) to return text like "Station('Grand Army Plaza', 6)"
# TODO: rebuild `fleet` from this class with the same loop as Step 2
# TODO: assign `van_list` to []; loop over `fleet`
# TODO: append each station whose needs_restock() returns True to `van_list`

print(van_list)
for station in van_list:
    print(station)

# Step 4, answer 1:
#
# Step 4, answer 2:
#
# Step 4, answer 3:
#
