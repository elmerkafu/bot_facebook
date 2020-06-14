from dotenv import load_dotenv
from pathlib import Path
import os
import random
from flask import Flask, request
from pymessenger.bot import Bot
from controllers.mensaje import message

MessageController = message()

app = Flask(__name__)

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
VERIFY_TOKEN = "prueba"
bot = Bot(ACCESS_TOKEN)

@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    else:
       output = request.get_json()
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                recipient_id = message['sender']['id']
                if message['message'].get('text'):
                    response_sent_text = get_message()
                    #agregar mensaje_bot
                    print(message['message'].get('text'))
                    print(response_sent_text)
                    MessageController.mensaje_user = 'hola'#message['message'].get('text')
                    MessageController.mensaje_bot = 'hola'#response_sent_text
                    MessageController.add_message(MessageController, app)
                    #termina problema
                    send_message(recipient_id, response_sent_text)
                if message['message'].get('attachments'):
                    response_sent_nontext = get_message()
                    send_message(recipient_id, response_sent_nontext)

    return "Message Processed"


def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'

def get_message():
    sample_responses = [
        "hola como estas", 
        "que estas buscando", 
        "contacte con nostros", 
        "hello :)"
        ]
    return random.choice(sample_responses)

def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    
    return "success"

if __name__ == "__main__":
    app.run()