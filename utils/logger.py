from loguru import logger

logger.add("logs/email.log", format="{time} - {level} - {message}", level="INFO", rotation="1 MB")
