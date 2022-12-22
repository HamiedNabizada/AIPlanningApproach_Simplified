(define (domain letseat-domain)
 (:requirements :strips :typing :negative-preconditions)
 (:types
    locatable location - object
    bot cupcake - locatable
    robot - bot
 )
 (:predicates (on ?obj - locatable ?loc - location) (holding ?arm - locatable ?cupcake - locatable) (arm_empty) (path ?location1 - location ?location2 - location))
 (:action pick_up
  :parameters ( ?arm_0 - bot ?cupcake - locatable ?loc - location)
  :precondition (and (not (on ?arm_0 ?loc)) (on ?cupcake ?loc) (arm_empty))
  :effect (and (not (on ?cupcake ?loc)) (holding ?arm_0 ?cupcake) (not (arm_empty))))
 (:action drop
  :parameters ( ?arm_0 - bot ?cupcake - locatable ?loc - location)
  :precondition (and (not (on ?arm_0 ?loc)) (holding ?arm_0 ?cupcake))
  :effect (and (on ?cupcake ?loc) (arm_empty) (not (holding ?arm_0 ?cupcake))))
 (:action move
  :parameters ( ?arm_0 - bot ?locfrom - location ?locto - location)
  :effect (and (not (on ?arm_0 ?locfrom)) (path ?locfrom ?locto)))
)
