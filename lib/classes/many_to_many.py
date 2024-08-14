class Article:
    # All of the articles can be stored in this list
    all= []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
    
    def __repr__(self):
        return f'<Article author={self.author} magazine={self.magazine} title={self.title} /> '
    
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        if(isinstance (value, str) and 5 <= len(value) <= 50 and not hasattr(self, 'title')):
            self._title = value
    
    # we need to do a property and an inistance to check that the magazine is an instance of Author 
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, value):
        if(isinstance(value, Author)):
            self._author = value

    # we need to do a property and an inistance to check that the magazine is an instance of Magaine 
    @property
    def magazine(self):
        return self._magazine
    @magazine.setter
    def magazine(self, value):
        if(isinstance(value, Magazine)):
            self._magazine = value




class Author:
    def __init__(self, name):
       self.name = name
    
    def __repr__(self): 
        return f'<Author name={self.name} />'
    

    @property
    def name(self):
        return self._name 
    @name.setter
    def name(self, value):
         if(isinstance(value, str) and len(value) > 0 and not hasattr(self, 'name')):
            self._name = value

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
       return Article (self, magazine, title)

    def topic_areas(self):
        # If there are no articles then return none and if there is return the list of strings but in an unique set
        # there will be a if not statement and we are going to need self.articles() to obtain all the articles.
        # We also need articel.magazine.category to extract the categories 
        if not self.articles():
            return None
        return list(set([article.magazine.category for article in self.articles()]))



class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    
    def __repr__(self):
        return f'<Magazine name={self.name} category={self.category} />'
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if(isinstance (value, str) and 2 <= len(value) <= 16):
            self._name = value
    
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, value):
        if(isinstance (value, str) and len(value) > 0):
            self._category = value
    


    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        # If there are no articles then return none and if there is return the list of title strings
        # there will be a if not statement and we are going to need self.articles() to obtain all the articles.
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        # We need to make a list that obtains all the authors in the articles if it is less than 2 return None if it is then return the list that does
        if len([article.author for article in self.articles()]) <= 2:
            return None
        return [article.author for article in self.articles()]
        
        
       