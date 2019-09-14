import unittest
from app.models import sources,Article

class sourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the news class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.news_source = sources('progm','program','Python Must Be Crazy','progrm.com','senior','en','england')

    def test_instance(self):
        self.assertTrue(isinstance(self.news_source,sources))

    def test_to_check(self):
        self.assertEquals(self.news_source.id,'progm')
        self.assertEquals(self.news_source.name,'progrm')
        self.assertEquals(self.news_source.description,'Python Must Be Crazy')
        self.assertEquals(self.news_source.url,'progrm.com')
        self.assertEquals(self.news_source.category,'senior')
        self.assertEquals(self.news_source.language,'en')
        self.assertEquals(self.news_source.country,'england')



class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the news class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_articles = Article('progm','bebe','programming','Python Must Be Crazy','progrm.com','techie.com/7643t94.jpg','2013-09-04TO7:12Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_artcles,Article))

    def test_to_check(self):
        self.assertEquals(self.new_articles.id,'progm')
        self.assertEquals(self.new_articles.name,'progrm')
         self.assertEquals(self.new_articles.title,'programming')
        self.assertEquals(self.new_articles.description,'Python Must Be Crazy')
        self.assertEquals(self.new_articles.url,'progrm.com')
        self.assertEquals(self.new_articles.image,'techie.com/7643t94.jpg')
        self.assertEquals(self.new_articles.date,'2013-09-04TO7:12Z')
