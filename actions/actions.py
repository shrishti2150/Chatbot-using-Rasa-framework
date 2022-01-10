# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet,EventType
import pyodbc 
#CURRENT=False 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SHRISHTIS_PB\SQLEXPRESS;'
                      'Database=Chat;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

#TRIAL
class PrintTable(Action):

    def name(self) -> Text:

        return "action_print_table"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        q="select * from DD_db"
        cursor.execute(q)
        result=cursor.fetchall()
        result=str(result)
        dispatcher.utter_message(result)
        return []

class AskForSlotAction(Action):

    def name(self) -> Text:

        return "ID_form"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        required_slots=["Username","Password"]
        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                return [SlotSet("requested_slot",slot_name)]

        #dispatcher.utter_message("Enter Password")
        return [SlotSet("requested_slot",slot_name)]

class ActionSubmit(Action):

    def name(self) -> Text:

        return "action_submit"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        

        dispatcher.utter_message(template="utter_details_thanks",Username=tracker.get_slot("Username"),Password=tracker.get_slot("Password"))
        return []

class StudentAttendance(Action):

    def name(self) -> Text:

        return "action_StudentAttendance"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        entities=tracker.latest_message['entities']
        print(entities)
        for e in entities:
            if e['entity']=='Username':
                q="exec Attendance @U="+e['value']+"@P="
        
        for e in entities:
            if e['entity']=='Password':
                q=q+e['value']+";"
        
        cursor.execute(q)
        result=cursor.fetchall()
        result=str(result)
        dispatcher.utter_message(result)
        return []

class Marks(Action):

    def name(self) -> Text:

        return "action_marks"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        entities=tracker.latest_message['entities']
        print(entities)
        for e in entities:
            if e['entity']=='Username':
                q="exec Q1MarksAccess @U="+e['value']+"@P="
        
        for e in entities:
            if e['entity']=='Password':
                q=q+e['value']+";"
        
        cursor.execute(q)
        result=cursor.fetchall()
        result=str(result)
        dispatcher.utter_message(result)
        return []
