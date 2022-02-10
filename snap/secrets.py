# for formatting purposes
class Config:
    def __init__(self):
        pass

    SECRET_KEY = "My secret key"

    # email config
    EMAIL_BACKEND = ""
    EMAIL_USE_TLS = True # Boolean
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_HOST_USER = "email address"
    EMAIL_HOST_PASSWORD = "pass"
    PORT = 465 # Port number
    development = True
    ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com', 'isnap.herokuapp.com'] 

    # Database config
    ENGINE = 'django.db.backends.postgresql_psycopg2',
    NAME = '<database_name>',
    USER = '<user_name>',
    PASSWORD = '<password>',
    HOST = 'localhost',
    DB_PORT = '',


config = Config()
