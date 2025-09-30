from models.user import User

class UserRepository:
    def __init__(self):
        self.usuarios = []
        self.next_id = 1

    def adicionar(self, nome, email):
        user = User(id=self.next_id, nome=nome, email=email)
        self.usuarios.append(user)
        self.next_id += 1
        return user

    def listar(self):
        return self.usuarios

    def desativar(self, user_id):
        for u in self.usuarios:
            if u.id == user_id:
                u.ativo = False
                return True
        return False
