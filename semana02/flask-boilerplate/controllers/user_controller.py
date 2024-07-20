class UserController:
    def create(self, json):
        return {
            'message': 'Usuario creado exitosamente'
        }, 201
    
    def get_all(self):
        return {
            'message': 'Listado de usuarios',
            'data': [
                {
                    'id': 1,
                    'name': 'Juan',
                }
            ]
        }, 200
    
    def get_by_id(self, id):
        return {
            'message': 'Usuario encontrado',
            'data': {
                'id': 1,
                'name': 'Juan',
            }
        }, 200
    
    def update(self, id, json):
        return {
            'message': 'Usuario actualizado exitosamente'
        }, 200