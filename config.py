import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey=3a10d7cd5abf4e089804482dab06b7bd'
    ALL_NEWS_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey=3a10d7cd5abf4e089804482dab06b7bd'

    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

  
