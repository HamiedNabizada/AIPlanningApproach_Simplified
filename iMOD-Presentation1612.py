import unified_planning
from unified_planning.shortcuts import *
import json
from unified_planning.io import PDDLWriter
# Stereotypen in SysML anschauen
# Types

# Move - Moving 
# Pick - Holding
# Drop - Releasing
# Transport - Conveying
Location = UserType('Location')
Locatable = UserType('Locatable')
Bot = UserType('Bot', Locatable)
TransportingGood = UserType('TransportingGood', Locatable)
TransportingRobot = UserType('TransportingRobot', Bot)
PickingRobot = UserType('PickingRobot', Bot)

# Predicates
at = Fluent('at', BoolType(), loc=Locatable, l=Location)  # Wo ist der Robi/Transportgut? True wenn Robi bei l ist dann True
connected = Fluent('connected', BoolType(), l_from=Location, l_to=Location)  # Gibt es eine Verbindung zwischen l_from und l_to
good_at = Fluent('good_at', BoolType(), tg=TransportingGood, lg=Location) #Prüfen ob notwendig (Transportgut an Position lg) # BRAUCHE ICH NICHT, ist duch at() abgedeckt
robot_occupied = Fluent('robot_occupied', BoolType(), tr=TransportingRobot) #Prüfen ob notwendig(Transport Roboter hat Transportgut beladen)


move = DurativeAction('move', b=Bot, l_from=Location, l_to=Location)
b = move.parameter('b')
l_from = move.parameter('l_from')
l_to = move.parameter('l_to')
move.set_fixed_duration(6)
move.add_condition(ClosedTimeInterval(StartTiming(), EndTiming()),  connected(l_from, l_to))
move.add_condition(StartTiming(), at(b, l_from))
move.add_effect(StartTiming(), at(b, l_from), False)
move.add_effect(EndTiming(), at(b, l_to), True)

pickup = DurativeAction('pickup', pb=PickingRobot, tr=TransportingRobot, ltr=Location, lpb=Location, tgpb=TransportingGood)
pb = pickup.parameter('pb')
tr = pickup.parameter('tr')
ltr = pickup.parameter('ltr')
lpb = pickup.parameter('lpb')
tgpb = pickup.parameter('tgpb')
pickup.set_fixed_duration(2)
pickup.add_condition(StartTiming(), good_at(tgpb, lpb)) # Transportgut muss an lpb sein
pickup.add_condition(StartTiming(), at(pb, lpb)) # PickingRobot muss auch da sein
pickup.add_condition(StartTiming(), connected(ltr, lpb)) #TransportRobot muss an einer Stelle sein, die direkt verbunden ist mit PickingPlace
pickup.add_condition(StartTiming(), at(tr, ltr))
pickup.add_condition(StartTiming(), Not(robot_occupied(tr))) #TransportRobot darf nichts anderes tragen
pickup.add_effect(EndTiming(), good_at(tgpb, lpb), False) # Nochmal drüber nachdenken, Transportgut "verschwindet" in der Zwischenzeit vom Schachbrett, wenn TR beladen
pickup.add_effect(EndTiming(), robot_occupied(tr), True)


drop = DurativeAction('drop', pb1=PickingRobot, tr1=TransportingRobot, ltr1=Location, lpb1=Location, tgpb1=TransportingGood)
pb1 = drop.parameter('pb1')
tr1 = drop.parameter('tr1')
ltr1 = drop.parameter('ltr1')
lpb1 = drop.parameter('lpb1')
tgpb1 = drop.parameter('tgpb1')
drop.set_fixed_duration(3)
drop.add_condition(StartTiming(), Not(good_at(tgpb1, lpb1)))
drop.add_condition(StartTiming(), at(pb1, lpb1))
drop.add_condition(StartTiming(), at(tr1, ltr1))
drop.add_condition(StartTiming(), connected(ltr1, lpb1))
drop.add_condition(StartTiming(), robot_occupied(tr1))
drop.add_effect(EndTiming(), good_at(tgpb1, lpb1), True)
drop.add_effect(EndTiming(), robot_occupied(tr1), False)


##############################################################################
# Problemgenerierung
problem = unified_planning.model.Problem('iMOD')
problem.add_fluent(at, default_initial_value=False)
problem.add_fluent(connected, default_initial_value=False)
problem.add_fluent(good_at, default_initial_value=False)
problem.add_fluent(robot_occupied, default_initial_value=False)
problem.add_action(pickup)
problem.add_action(move)
problem.add_action(drop)
# Einlesen der JSON-File
f = open('informationsCE.json')
data = json.load(f)
f.close()
# Anreichern der Daten mit "Verbundenheit" (keine Diagonalen)
workingpoints = data['workingpoints']
robotdata = data['robots']
for i in workingpoints:
    connectedTemp = []
    for j in workingpoints:
        if (abs(i['x']-j['x']) == 0 and abs(i['y']-j['y']) == 1) or (abs(i['x']-j['x']) == 1 and abs(i['y']-j['y']) == 0):
            connectedTemp.append(j['id'])
    i['connectedTo'] = connectedTemp
locations = []
for i in workingpoints:
    locations.append(unified_planning.model.Object(i['id'], Location))


for i in locations:
    for j in workingpoints:
        if i.name == j['id']:
            for k in j['connectedTo']:
                for l in locations:
                    if k == l.name:
                        problem.set_initial_value(connected(i, l), True)
problem.add_objects(locations)
# Roboter
availableRobots = []
for i in robotdata:
    for j in i["capabilites"]:
        if(j=="picking"):
            availableRobots.append(unified_planning.model.Object(i['id'], PickingRobot))
        if(j=="transporting"):
            availableRobots.append(unified_planning.model.Object(i['id'], TransportingRobot))
for i in availableRobots:
    for j in robotdata:
        if i.name == j['id']:
            for k in locations:
                if k.name == j['currentLocation']:
                    problem.set_initial_value(at(i, k), True)
problem.add_objects(availableRobots)

transportGood = unified_planning.model.Object('transportGood', TransportingGood)
problem.add_object(transportGood)

problem.set_initial_value(good_at(transportGood, locations[10]), True)
problem.add_goal(good_at(transportGood, locations[-1]))

w = PDDLWriter(problem)

w.write_domain('domain1612.pddl')
w.write_problem('problem1612.pddl')
with OneshotPlanner(problem_kind=problem.kind) as planner:
    result = planner.solve(problem)
    plan = result.plan
    if plan is not None:
        print("%s returned:" % planner.name)
        for start, action, duration in plan.timed_actions:
            print("%s: %s [%s]" % (float(start), action, float(duration)))
    else:
        print("No plan found.")