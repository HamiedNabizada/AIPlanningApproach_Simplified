(define (problem letseat-problem)
 (:domain letseat-domain)
 (:objects
   table plate - location
   arm1 - robot
   cupcake1 - cupcake
 )
 (:init (on arm1 table) (on cupcake1 table) (arm_empty) (path table plate))
 (:goal (and (on cupcake1 plate)))
)
