import spacy
from googleapiclient.discovery import build  #pip install google-api-python-client  

user_context = {}

def track_context(user_id, message):
    if user_id not in user_context:
        user_context[user_id] = {'history':[]}
    user_context[user_id]['history'].append(message)


nlp = spacy.load('en_core_web_sm')

def extract_context(message):
    doc = nlp(message)
    entities = [(ent.text, ent.label) for ent in doc.ents]
    return entities

def recommend_action(user_context):
    last_message = user_context['history'][-1].lower()
    # if else statement needed related to  json file
    pass

def get_calender_events(user_id):
    service = build('calender', 'v3', credentials=user_credentials[user_id])
    events = service.events().list(calenderOd = 'primary').execute()
    return events

def recommend_from_calender(events):
    if events:
        return f"Meeting '{events[0]['summary']} coming up."
    else: 
        return 'No upcoming events.'
    
def chat_response(user_id, user_message):
    track_context(user_id, user_message)
    entities = extract_context(user_message)
    recommendation = recommend_action(user_context[user_id])
    return recommendation