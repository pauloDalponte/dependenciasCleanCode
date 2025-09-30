from utils.logger import logger

class EmailService:
    def enviar_boas_vindas(self, usuario):
        mensagem = f"Olá {usuario.nome}, bem-vindo ao sistema!"
        print(f"[EMAIL SIMULADO] Enviando para {usuario.email}: {mensagem}")
        logger.info(f"Email enviado para {usuario.email}: {mensagem}")
