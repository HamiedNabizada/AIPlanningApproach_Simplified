(define (domain imod-domain)
 (:requirements :strips :typing :equality :numeric-fluents :durative-actions)
 (:types
    robots location - object
    millingrobot - robots
 )
 (:predicates (robot_at ?r - robots ?l - location) (connected ?l_from - location ?l_to - location) (milled ?lo - location))
 (:functions (occupied ?lo - location))
 (:durative-action move
  :parameters ( ?r - robots ?l_from - location ?l_to - location)
  :duration (= ?duration 6)
  :condition (and (at start (connected ?l_from ?l_to))(at start (robot_at ?r ?l_from))(at start (= (occupied ?l_to) 0))(over all (= (occupied ?l_to) 0))(at end (= (occupied ?l_to) 0)))
  :effect (and (at start (not (robot_at ?r ?l_from))) (at start (assign (occupied ?l_from) (- (occupied ?l_from) 1))) (at end (robot_at ?r ?l_to)) (at end (assign (occupied ?l_to) (+ 1 (occupied ?l_to))))))
 (:durative-action mill
  :parameters ( ?rm - millingrobot ?lm - location)
  :duration (= ?duration 10)
  :condition (and (at start (robot_at ?rm ?lm)))
  :effect (and (at end (milled ?lm))))
)
