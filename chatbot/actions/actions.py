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
            sub_entity = send_request_to_typedb(f"match $e sub entity;")
            buttons_list = []
            for s in sub_entity:
                buttons_name = str(s.get('e')._label)
                if not buttons_name == "entity":
                    buttons_list.append({"payload": "/query_entity{\"entity\":\""+buttons_name+"\"}", "title": buttons_name})
            dispatcher.utter_message(text=f"Je ne parviens pas à trouver ce que vous me demandez. Que cherchez-vous exactement?", buttons=buttons_list)
        return []

class Action_Query_All_Attribute_Of_Entity(Action):

    def name(self) -> Text:
        return "action_query_all_attribute_of_entity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        intent_entities = tracker.latest_message.get("entities")
        entity_type = has_entity_type(intent_entities, "value_attribute")

        entity_attr = None

        try:
            if(entity_type):
                entity_attr = send_request_to_typedb(f"match $x isa entity, has attribute \"{entity_type[0]}\", has $attr; $attr isa! $attr-type; get $attr-type;")
        except:
            pass

        if entity_attr:
            buttons_list = []
            for attr in entity_attr:
                attr_button_name = str(attr.get('attr-type')._label)
                buttons_list.append({"payload": "/query_attribute{\"attribute\":\""+attr_button_name+"\", \"value_attribute\":\""+entity_type[0]+"\"}", "title": attr_button_name})
            dispatcher.utter_message(text="Que voulez vous savoir exactement?", buttons=buttons_list)
        else:
            dispatcher.utter_message("Je n'ai pas bien compris ce que vous vouliez savoir")

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