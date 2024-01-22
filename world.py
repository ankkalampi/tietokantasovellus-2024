## This module handles world (npc group) related tasks.
## This includes the following functionality:
##  - create and delete worlds
##  - load world based on world id
##  - get worlds based on current user
## A world has the following properties:
##  - name (string)
##  - id (int)
##  - user_id (int)
##  - global_events (list (int event_id))