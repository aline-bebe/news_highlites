import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_SOURCES_URL = "https://newsapi.org/v2/sources?apiKey={}"
    NEWS_ARTICLE_URL = "https://newsapi.org/v2/top-headlines?sources={}&apiKey={}"
    # NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    NEWS_API_KEY = "d1d5dd7661a04cca92cea42201c77856"


class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
