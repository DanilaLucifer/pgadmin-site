"""
Пример использования библиотеки pgadmin_site.
"""

from pgadmin_site import site

if __name__ == "__main__":
    # Запустить локальный сайт для работы с базой данных
    site(
        host="localhost",
        port=5432,
        username="postgres",
        password="your_password",  # Замените на ваш пароль
        database="your_database",  # Замените на имя вашей базы данных
        web_port=5000,             # Порт для веб-интерфейса
        debug=True                 # Режим отладки
    ) 