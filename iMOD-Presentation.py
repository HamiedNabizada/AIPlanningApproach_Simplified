import unified_planning
from unified_planning.shortcuts import *
from unified_planning.io import PDDLReader, PDDLWriter


# Typiserung
Location = UserType('Location')
Locatable = UserType('Locatable')
Bot = UserType('Bot', Locatable)
Cupcake = UserType('Cupcake', Locatable)
Robot = UserType('Robot', Bot)

# Fluents and constants
on = Fluent('on', BoolType(), obj = Locatable, loc = Location)
holding = Fluent('holding', BoolType(), arm = Locatable, cupcake = Locatable)
arm_empty = Fluent('arm_empty', BoolType())
path = Fluent('path', BoolType(), location1 = Location, location2 = Location)

# Actions
pick_up = InstantaneousAction('pick_up', arm=Bot, cupcake=Locatable, loc=Location)
arm = pick_up.parameter('arm')
cupcake = pick_up.parameter('cupcake')
loc = pick_up.parameter('loc')
pick_up.add_precondition(Not(on(arm, loc)))
pick_up.add_precondition(on(cupcake, loc))
pick_up.add_precondition(arm_empty)
pick_up.add_effect(on(cupcake, loc), False)
pick_up.add_effect(holding(arm, cupcake), True)
pick_up.add_effect(arm_empty, False)

drop = InstantaneousAction('drop', arm=Bot, cupcake=Locatable, loc=Location)
arm = drop.parameter('arm')
cupcake = drop.parameter('cupcake')
loc = drop.parameter('loc')
drop.add_precondition(Not(on(arm, loc)))
drop.add_precondition(holding(arm, cupcake))
drop.add_effect(on(cupcake, loc), True)
drop.add_effect(arm_empty, True)
drop.add_effect(holding(arm, cupcake), False)

move = InstantaneousAction('move', arm=Bot, locFrom=Location, locTo=Location)
arm = move.parameter('arm')
locFrom = move.parameter('locFrom')
locTo = move.parameter('locTo')
move.add_effect(on(arm, locFrom), False)
move.add_effect(path(locFrom, locTo), True)

problem = Problem('letseat')
problem.add_fluent(on, default_initial_value=False)
problem.add_fluent(holding, default_initial_value=False)
problem.add_fluent(arm_empty, default_initial_value=False)
problem.add_fluent(path, default_initial_value=False)
problem.add_action(pick_up)
problem.add_action(drop)
problem.add_action(move)

arm1 = Object("arm1", Robot)
cupcake1 = Object('cupcake1', Cupcake)
table = Object("table", Location)
plate = Object("plate", Location)

problem.add_object(arm1)

problem.add_object(cupcake1)
problem.add_object(table)
problem.add_object(plate)

problem.set_initial_value(on(arm1, table), True)
problem.set_initial_value(on(cupcake1, table), True)
problem.set_initial_value(arm_empty, True)
problem.set_initial_value(path(table, plate), True)

problem.add_goal(on(cupcake1, plate))

w = PDDLWriter(problem)
print(w.get_domain())
print("-------")
w.write_domain('presentation_domain.pddl')
w.write_problem('presentation_problem.pddl')


with OneshotPlanner(problem_kind=problem.kind) as planner:
    result = planner.solve(problem)
    plan = result.plan
    if plan is not None:
        print("%s returned:" % planner.name)
        for start, action, duration in plan.timed_actions:
            print("%s: %s [%s]" % (float(start), action, float(duration)))
    else:
        print("No plan found.")
