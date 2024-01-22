## This module controls dialogue creation and execution.
## This includes the following functionality:
##  - creation and destruction of dialogue components
##  - creating dialogue components from topics
##  - opening and closing dialogue execution
##  - presenting list of current dialogue options based on dialogue option requirements
##  - executing dialogue option (present option text and load new list of dialogue options)
##
## Dialogue components consist of dialogue options.
## Dialogue option can be a start of a topic, end of a topic, or in the middle of a topic.
## Dialogue option has requirements and following options.
## Dialogue options have the following properties:
##  - name (string)
##  - id (int)
##  - titles                (dict -> key: conduct (enum)    value: title (string)) -> this is what is displayed as the option
##  - texts                 (dict -> key: conduct (enum)    value: text (string)) -> this is what is displayed as npc reaction
##  - required_dialogues    (list (int option_id)) pass if null
##  - required_personality (enum personality)
##  - required_player_emotion (enum emotion) pass if null
##  - requird_base_emotion (enum emotion) pass if null
##  - required_events (list (int event_id)) pass if null
##  - type (enum option_type -> can be: start, middle, end   start loads topic, middle loads leads_to, end loads dialogue begin topic)
##  - leads_to (list option_id) pass if type is start or end
## Topics have the following properties:
##  - name (string)
##  - id (int)
##  - title (string) -> this is what is displayed
##  - required_events (list (int event_id)) pass if null
##  - required_player_emotion (enum emotion)
##  - required_base_emotion (enum emotion)
##  - required_personality (enum personality)
## Dialogues have the following properties:
##  - name (string)
##  - id (int)
##  - topics (list (int topc_id)) 
##


