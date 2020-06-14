from models.mensaje import mensajes
from helpers.helper import handler_response
from App import app

class message:
    def add_message(self, app):
        try:
            mensajes.insert({
                'mensaje_user': 'olaa',
                'mensaje_bot': 'hola',
                'fecha': 'current_date'
            })  
            return handler_response(app, 201, f'Se creo el mensaje')
        except Exception as e:
            return handler_response(app, 500, str(e))


MessageController = message()
MessageController.add_message(app)

