(define (problem imod-problem)
  (:domain imod-domain)
  (:objects
    loc00 loc10 loc20 loc30 loc40 loc50 loc60 loc01 loc11 loc21 loc31 loc41 loc51 loc61 loc02 loc12 loc22 loc32 loc42 loc52 loc62 - location
    transportgood - transportinggood
    robot2 - transportingrobot
    robot1 - pickingrobot
  )
  (:init
    (connected loc00 loc10)
    (connected loc00 loc01)
    (connected loc10 loc00)
    (connected loc10 loc20)
    (connected loc10 loc11)
    (connected loc20 loc10)
    (connected loc20 loc30)
    (connected loc20 loc21)
    (connected loc30 loc20)
    (connected loc30 loc40)
    (connected loc30 loc31)
    (connected loc40 loc30)
    (connected loc40 loc50)
    (connected loc40 loc41)
    (connected loc50 loc40)
    (connected loc50 loc60)
    (connected loc50 loc51)
    (connected loc60 loc50)
    (connected loc60 loc61)
    (connected loc01 loc00)
    (connected loc01 loc11)
    (connected loc01 loc02)
    (connected loc11 loc10)
    (connected loc11 loc01)
    (connected loc11 loc21)
    (connected loc11 loc12)
    (connected loc21 loc20)
    (connected loc21 loc11)
    (connected loc21 loc31)
    (connected loc21 loc22)
    (connected loc31 loc30)
    (connected loc31 loc21)
    (connected loc31 loc41)
    (connected loc31 loc32)
    (connected loc41 loc40)
    (connected loc41 loc31)
    (connected loc41 loc51)
    (connected loc41 loc42)
    (connected loc51 loc50)
    (connected loc51 loc41)
    (connected loc51 loc61)
    (connected loc51 loc52)
    (connected loc61 loc60)
    (connected loc61 loc51)
    (connected loc61 loc62)
    (connected loc02 loc01)
    (connected loc02 loc12)
    (connected loc12 loc11)
    (connected loc12 loc02)
    (connected loc12 loc22)
    (connected loc22 loc21)
    (connected loc22 loc12)
    (connected loc22 loc32)
    (connected loc32 loc31)
    (connected loc32 loc22)
    (connected loc32 loc42)
    (connected loc42 loc41)
    (connected loc42 loc32)
    (connected loc42 loc52)
    (connected loc52 loc51)
    (connected loc52 loc42)
    (connected loc52 loc62)
    (connected loc62 loc61)
    (connected loc62 loc52)
    (at_ robot1 loc00)
    (at_ robot2 loc02)
    (good_at transportgood loc31)
  )
  (:goal
    (and (good_at transportgood loc62))
  )
)