(define (domain imod-domain)
   (:requirements :strips :typing :negative-preconditions :durative-actions)
   (:types
      locatable location - object
      transportinggood bot - locatable
      transportingrobot pickingrobot - bot
   )
   (:predicates
      (at_ ?loc - locatable ?l - location)
      (connected ?l_from - location ?l_to - location)
      (good_at ?tg - transportinggood ?lg - location)
      (robot_occupied ?tr - transportingrobot)
   )
   (:durative-action pickup
      :parameters ( ?pb - pickingrobot ?tr - transportingrobot ?ltr - location ?lpb - location ?tgpb - transportinggood)
      :duration (= ?duration 2)
      :condition (and (at start (good_at ?tgpb ?lpb))
         (at start (at_ ?pb ?lpb))
         (at start (connected ?ltr ?lpb))
         (at start (at_ ?tr ?ltr))
         (at start (not (robot_occupied ?tr))))
      :effect (and (at end (not (good_at ?tgpb ?lpb))) (at end (robot_occupied ?tr)))
   )
   (:durative-action move
      :parameters ( ?b - bot ?l_from - location ?l_to - location)
      :duration (= ?duration 6)
      :condition (and (at start (connected ?l_from ?l_to))
         (over all (connected ?l_from ?l_to))
         (at end (connected ?l_from ?l_to))
         (at start (at_ ?b ?l_from)))
      :effect (and (at start (not (at_ ?b ?l_from))) (at end (at_ ?b ?l_to)))
   )
   (:durative-action drop
      :parameters ( ?pb1 - pickingrobot ?tr1 - transportingrobot ?ltr1 - location ?lpb1 - location ?tgpb1 - transportinggood)
      :duration (= ?duration 3)
      :condition (and (at start (not (good_at ?tgpb1 ?lpb1)))
         (at start (at_ ?pb1 ?lpb1))
         (at start (at_ ?tr1 ?ltr1))
         (at start (connected ?ltr1 ?lpb1))
         (at start (robot_occupied ?tr1)))
      :effect (and (at end (good_at ?tgpb1 ?lpb1)) (at end (not (robot_occupied ?tr1))))
   )
)