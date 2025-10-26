import logging


def log_user_action(user_id: int, action: str):
    logging.info(f"Пользователь {user_id} выполнил: {action}")
