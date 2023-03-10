(define (problem imod-problem)
  (:domain imod-domain)
  (:objects
    loc00 loc10 loc20 loc30 loc40 loc50 loc60 loc01 loc11 loc21 loc31 loc41 loc51 loc61 loc02 loc12 loc22 loc32 loc42 loc52 loc62 - location
    robot1 robot2 - millingrobot
  )
  (:init
    (robot_at robot1 loc00)
    (= (occupied loc00) 1)
    (milled loc00)
    (robot_at robot2 loc02)
    (= (occupied loc02) 1)
    (milled loc02)
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
    (= (occupied loc10) 0)
    (= (occupied loc20) 0)
    (= (occupied loc30) 0)
    (= (occupied loc40) 0)
    (= (occupied loc50) 0)
    (= (occupied loc60) 0)
    (= (occupied loc01) 0)
    (= (occupied loc11) 0)
    (= (occupied loc21) 0)
    (= (occupied loc31) 0)
    (= (occupied loc41) 0)
    (= (occupied loc51) 0)
    (= (occupied loc61) 0)
    (= (occupied loc12) 0)
    (= (occupied loc22) 0)
    (= (occupied loc32) 0)
    (= (occupied loc42) 0)
    (= (occupied loc52) 0)
    (= (occupied loc62) 0)
  )
  (:goal
    (and (milled loc00) (milled loc10) (milled loc20) (milled loc30) (milled loc40) (milled loc50) (milled loc60) (milled loc01) (milled loc11) (milled loc21) (milled loc31) (milled loc41) (milled loc51) (milled loc61) (milled loc02) (milled loc12) (milled loc22) (milled loc32) (milled loc42) (milled loc52) (milled loc62))
  )
)