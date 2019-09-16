from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_news, get_articles
from ..models import Source, Article

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    news_source = get_news('category')
    
    title = "Welcome to News Highlight"
    return render_template('index.html', title = title, sources = news_source)

@main.route('/news/<id>')
def news (id):
    '''
    Returns the news article from a highlight
    '''
    news_args = get_articles(id)
    return render_template("articles.html", news=news_args)
