import spacy

user_context = {}

def track_context(user_id, message):
    if user_id not in user_context:
        user_context[user_id] = {'history':[]}
    user_context[user_id]['history'].append(message)


