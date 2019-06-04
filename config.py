import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    APP = os.environ.get('APP_NAME') or 'MiCro::'
    if os.environ.get('SECRET_KEY'):
        SECRET_KEY = os.environ.get('SECRET_KEY')
    else:
        SECRET_KEY = 'SECRET_KEY_ENV_VAR_NOT_SET'
        print('   SECRET KEY ENV VAR NOT SET! SHOULD NOT SEE IN PRODUCTION')
        SQLALCHEMY_COMMIT_ON_TEARDOWN = False

    # Admin account
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD') or 'demo1'
    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL') or 'admin@admin.com'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
