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
                    insertar(
                        message['message'].get('text'),
                        response_sent_text,
                        recipient_id
                    )
                    send_message(recipient_id, response_sent_text)
                if message['message'].get('attachments'):
                    response_sent_nontext = get_message()
                    send_message(recipient_id, response_sent_nontext)

    return "Message Processed"


def insertar(mensaje_user, mensaje_bot, id_usuario):
    MessageController.mensaje_user = mensaje_user
    MessageController.mensaje_bot = mensaje_bot
    MessageController.id_usuario = id_usuario
    return MessageController.add_message(MessageController, app)

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