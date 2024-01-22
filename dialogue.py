## This module controls dialogue creation and execution.
## This includes the following functionality:
##  - creation and destruction of dialogue components
##  - creating dialogue components from subdialogues
##  - opening and closing dialogue execution
##  - presenting list of current dialogue options based on dialogue option requirements
##  - executing dialogue option (present option text and load new list of dialogue options)
##
## Dialogue components consist of subdialogues.
## Subdialogues consist of dialogue options.
## Dialogue options have the following properties:
##  - name (string)
##  - id (int)
##  - titles                (dict -> key: conduct (enum)    value: title (string)) -> this is what is displayed as the option
##  - texts                 (dict -> key: conduct (enum)    value: text (string)) -> this is what is displayed as npc reaction
##  - required_dialogues    (list (int dialogue_id)    
