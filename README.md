# AIPlanningApproach_Simplified

This repository is intended to demonstrate a simplified use case representing research on automated sequencing in iMOD. In its current state, the use case involves a simple pick and place operation by two TurtleBots. One of the TurtleBots is equipped with a gripper arm and has the ability to pick something up and place it on another TurtleBot. The other TurtleBot is purely responsible for transport. 

In the current state, a JSON file is taken as input, which contains information about the generation of the PDDL domain and problem file. The Python-based [Unified Planning Framework](https://github.com/aiplan4eu/unified-planning) is used for this generation. For problem solving (not included in this repository), [Planutils](https://github.com/AI-Planning/planutils) is used, which contains easy access to a variety of PDDL solvers.

