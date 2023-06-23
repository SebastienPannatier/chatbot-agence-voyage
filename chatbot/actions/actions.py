from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typedb.client import *

def has_entity_type(entities, type):
    res = list()
    for e in entities:
        if e["entity"] == type:
            res.append(e["value"])
    if len(res) < 1:
        res = False
    return res

def send_request_to_typedb(rqte):
    with TypeDB.core_client("localhost:1729") as client:
        with client.session("agence-de-voyage", SessionType.DATA) as session:
            with session.transaction(TransactionType.READ) as read_transaction:
                try:
                    res = read_transaction.query().match(rqte)
                    res = list(res)
                except:
                    res = list([False])
                
                return res

def get_all_attribute_of_entity(entity):
    request = f"match $x isa {entity}, has $attr; $attr isa! $attr-type; get $attr-type;"
    result = send_request_to_typedb(request)
    return result

class Action_Query_entity(Action):

    def name(self) -> Text:
        return "action_query_entity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        intent_entities = tracker.latest_message.get("entities")
        entity_type = has_entity_type(intent_entities, "entity")

        if entity_type == False:
            result = [False]
        else:
            result = send_request_to_typedb(f"match $x isa {entity_type[0]}, has nom $nom;")


        if result[0] != False:
            dispatcher.utter_message(f"Voici les {entity_type[0]}s que j'ai trouvé:")
            for r in result:
                dispatcher.utter_message(f"{r.get('nom')._value}")
        else:
            dispatcher.utter_message(text=f"Je ne parviens pas à trouver ce que vous me demandez. Que cherchez-vous exactement?", buttons=[{"payload":"/query_entity{\"entity\":\"restaurant\"}", "title":"Restaurant"},{"payload":"/query_entity{\"entity\":\"hotel\"}", "title":"Hotel"}])
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