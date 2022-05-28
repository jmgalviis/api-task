class Config:
    ...


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin123@localhost/api'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'th1s1sS3cr3t'


config = {
    'development': DevelopmentConfig
}
