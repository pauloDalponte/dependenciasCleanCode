from repositories.user_repository import UserRepository
from services.email_service import EmailService
from services.api_service import buscar_usuario_api
from models.user import User

class App:
    def __init__(self):
        self.user_repo = UserRepository()
        self.email_service = EmailService()

    def adicionar_usuario(self, nome: str, email: str):
        user = self.user_repo.adicionar(nome, email)
        self.email_service.enviar_boas_vindas(user)
        return user

    def listar_usuarios(self):
        return self.user_repo.listar()

    def desativar_usuario(self, user_id: int):
        return self.user_repo.desativar(user_id)

    def buscar_usuario_api(self, user_id: int):
        return buscar_usuario_api(user_id)
