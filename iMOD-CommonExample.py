# Example for presentation on 16.12.
import json
import unified_planning
from unified_planning.shortcuts import *
from unified_planning.io import PDDLReader, PDDLWriter

# Einlesen der JSON-File
f = open('informationsCE.json')
data = json.load(f)
f.close()
workingpoints = data['workingpoints']
robotdata = data['robots']

# Typiserung
Location = UserType('Location')
Robots = UserType('Robots')
PickingRobot = UserType('PickingRobot', Robots)
TransportingRobot = UserType('TransportingRobot', Robots)

# Fluents and constants
robot_at = unified_planning.model.Fluent('robot_at', BoolType(), r=Robots, l=Location)  # Wo ist der Robi? True wenn Robi bei l ist dann True
connected = unified_planning.model.Fluent('connected', BoolType(), l_from=Location, l_to=Location)  # Gibt es eine Verbindung zwischen l_from und l_to
occupied = unified_planning.model.Fluent('occupied', RealType(0, 1), lo=Location) #Testing Variable

# Actions
move = DurativeAction('move', r=Robots, l_from=Location, l_to=Location)
r = move.parameter('r')
l_from = move.parameter('l_from')
l_to = move.parameter('l_to')
move.set_fixed_duration(6)
move.add_condition(StartTiming(), connected(l_from, l_to))
move.add_condition(StartTiming(), robot_at(r, l_from))
move.add_effect(StartTiming(), robot_at(r, l_from), False)
move.add_effect(EndTiming(), robot_at(r, l_to), True)

pickup = DurativeAction('pickup', pr=PickingRobot, pl=Location, pd=Location)