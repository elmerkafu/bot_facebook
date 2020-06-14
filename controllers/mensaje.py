from models.mensaje import mensajes as MensajeModel
from helpers.helper import handler_response

class message:
    def add_message(self, mensaje, app):
        try:
            MensajeModel.insert({
                'mensaje_user': mensaje.mensaje_user,
                'mensaje_bot': mensaje.mensaje_bot,
                'id_usuario': mensaje.id_usuario
            })  
            return handler_response(app, 201, f'Se creo el mensaje')
        except Exception as e:
            return handler_response(app, 500, str(e))



