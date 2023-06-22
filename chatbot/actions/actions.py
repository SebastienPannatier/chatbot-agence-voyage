from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class Action_Query_entity(Action):

    def name(self) -> Text:
        return "action_query_entity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="action_query_entity")

        return []

class Action_Query_All_Attribute_Of_Entity(Action):

    def name(self) -> Text:
        return "action_query_all_attribute_of_entity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="action_query_all_attribute_of_entity")

        return []
    
class Action_Query_Entity_By_Attribute(Action):

    def name(self) -> Text:
        return "action_query_entity_by_attribute"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="action_query_entity_by_attribute")

        return []
    
class Action_Query_Attribute(Action):

    def name(self) -> Text:
        return "action_query_attribute"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="action_query_attribute")

        return []