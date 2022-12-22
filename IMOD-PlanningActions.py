
import json
import unified_planning
from unified_planning.shortcuts import *
from unified_planning.io import PDDLReader, PDDLWriter

from math import dist

# Einlesen der JSON-File
f = open('informations.json')
data = json.load(f)
f.close()
workingpoints = data['workingpoints']
robotdata = data['robots']


# Typiserung
Location = UserType('Location')
Robots = UserType('Robots')
MillingRobot = UserType('MillingRobot', Robots)
RivetingRobot = UserType('RivetingRobot', Robots)

# Fluents and constants
robot_at = unified_planning.model.Fluent('robot_at', BoolType(), r=Robots, l=Location)  # Wo ist der Robi? True wenn Robi bei l ist dann True
connected = unified_planning.model.Fluent('connected', BoolType(), l_from=Location, l_to=Location)  # Gibt es eine Verbindung zwischen l_from und l_to
occupied = unified_planning.model.Fluent('occupied', RealType(0, 1), lo=Location) #Testing Variable

milled = unified_planning.model.Fluent('milled', BoolType(), lo=Location) 
riveted = unified_planning.model.Fluent('riveted', BoolType(), lo=Location)
# TODO: Milled und Riveted Fluent hinzufügen
# Actions
move = DurativeAction('move', r=Robots, l_from=Location, l_to=Location)
r = move.parameter('r')
l_from = move.parameter('l_from')
l_to = move.parameter('l_to')
move.set_fixed_duration(6)
move.add_condition(StartTiming(), connected(l_from, l_to))
move.add_condition(StartTiming(), robot_at(r, l_from))
move.add_condition(ClosedTimeInterval(StartTiming(), EndTiming()), Equals(occupied(l_to), 0))
move.add_effect(StartTiming(), robot_at(r, l_from), False)
move.add_effect(EndTiming(), robot_at(r, l_to), True)
move.add_effect(StartTiming(), occupied(l_from), Minus(occupied(l_from), 1))
move.add_effect(EndTiming(), occupied(l_to), Plus(occupied(l_to), 1))

mill = DurativeAction('mill', rM=MillingRobot, lM=Location)
rM = mill.parameter('rM')
lM = mill.parameter('lM')
mill.set_fixed_duration(10)
mill.add_condition(StartTiming(), robot_at(rM, lM))
#mill.add_condition(StartTiming(), milled(lM), False)
mill.add_effect(EndTiming(), milled(lM), True)

# Problemgenerierung
problem = unified_planning.model.Problem('iMOD')
problem.add_fluent(robot_at, default_initial_value=False)
problem.add_fluent(connected, default_initial_value=False)
problem.add_fluent(occupied, default_initial_value=0)
problem.add_fluent(milled, default_initial_value=False)
problem.add_action(move)
problem.add_action(mill)

# Prüfen welche Locations direkt miteinander verbunden sind (Keine diagonalen Wege)
for i in workingpoints:
    connectedTemp = []
    for j in workingpoints:
        if (abs(i['x']-j['x']) == 0 and abs(i['y']-j['y']) == 1) or (abs(i['x']-j['x']) == 1 and abs(i['y']-j['y']) == 0):
            connectedTemp.append(j['id'])
    i['connectedTo'] = connectedTemp

locations = []
for i in workingpoints:
    locations.append(unified_planning.model.Object(i['id'], Location))


problem.add_objects(locations)
availableRobots = []
for i in robotdata:
    availableRobots.append(unified_planning.model.Object(i['id'], MillingRobot))

for i in availableRobots:
    for j in robotdata:
        if i.name == j['id']:
            for k in locations:
                if k.name == j['currentLocation']:
                    problem.set_initial_value(robot_at(i, k), True)
                    problem.set_initial_value(occupied(k), 1)

problem.add_objects(availableRobots)

for i in locations:
    for j in workingpoints:
        if i.name == j['id']:
            for k in j['connectedTo']:
                for l in locations:
                    if k == l.name:
                        problem.set_initial_value(connected(i, l), True)

for i in locations:
    problem.add_goal(milled(i))
#problem.add_goal(robot_at(availableRobots[0], locations[-1]))
#problem.add_goal(robot_at(availableRobots[1], locations[6]))
w = PDDLWriter(problem)
print(w.get_domain())
print("-------")
w.write_domain('testing_domain.pddl')
w.write_problem('testing_problem.pddl')


with OneshotPlanner(problem_kind=problem.kind) as planner:
    result = planner.solve(problem)
    plan = result.plan
    if plan is not None:
        print("%s returned:" % planner.name)
        for start, action, duration in plan.timed_actions:
            print("%s: %s [%s]" % (float(start), action, float(duration)))
    else:
        print("No plan found.")
