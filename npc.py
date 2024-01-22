## This module controls how npc:s generate emotios towards the player
## as well as different topics. 
## An NPC object has the following properties:
##  - name (string)
##  - personality (enum personality)
##  - player_emotion (enum emotion)
##  - base_emotion  (enum emotion)
##  - topic_emotions    (dict ->    key: topic_id       value: enum emotion)
##  - reactions         (dict ->    key: global_event   value: enum emotion)
## NPC module has the following functionality:
##  - create and destroy npc data (in/from database)
##  - generate NPC from database data
##  - calculate player_emotion based on personality and reactions
##  - calculate conduct based on base_emotion, player_emotion, and topic_emotions