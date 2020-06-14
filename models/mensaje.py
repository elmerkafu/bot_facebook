from database.connection import Conexion

conn = Conexion()
Model = conn.model()

class mensajes(Model):
    __table__ = 'mensaje'
    __primary_key__ = 'id_mensaje'
    __timestamps__ = True
    __connection__ = 'postgres'

    __guarded__ = ['id_mensaje']

    __fillable__ = ['mensaje_user', 'mensaje_bot', 'fecha']

    __casts__ = {
        'mensaje_user': 'str',
        'mensaje_bot': 'str',
        'fecha': 'str'
    }


