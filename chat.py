import random
import json
import torch
import webbrowser
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
import spacy
from googleapiclient.discovery import build 

nlp = spacy.load('en_core_web_sm') #python -m spacy download en_core_web_sm

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as f:
    intents = json.load(f)

FILE = 'data.pth'
data = torch.load(FILE)

input_size = data['input_size']
hidden_size = data['hidden_size']
output_size = data['output_size']
all_words = data['all_words']
tags = data['tags']
model_state = data['model_state']

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

sites = {
    'open_github': 'https://github.com/Jitenrai21/ChatterMate',
    'open_youtube': 'https://www.youtube.com/',
    'open_chatgpt': 'https://chatgpt.com/'
}

bot_name = 'ChatterMate'
user_context = {}

print("Let's chat! Press 'Q' to exit.")
while True:
    sentence = input('You: ')
    if sentence.lower() == 'q':
        break

    sentence = tokenize(sentence)
    x = bag_of_words(sentence, all_words)
    x = x.reshape(1, x.shape[0])
    x = torch.from_numpy(x)

    output = model(x)

    _, predicted = torch.max(output, dim = 1)
    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        if tag in sites:
            print(f"{bot_name}: Opening {tag.replace('_', ' ').title()}...")
            webbrowser.open(sites[tag])
        else:
            for intent in intents['intents']:
                if tag == intent['tag']:
                    if '_help' in tag:
                        combined_response = '\n'.join(intent['responses'])
                        print(f'{bot_name}: {combined_response}')
                    else:
                        print(f"{bot_name}: {random.choice(intent['responses'])}")
    
    else:
        print(f"{bot_name}: I'm not sure how to help with that. :(")
