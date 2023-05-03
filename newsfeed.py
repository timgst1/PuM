from abc import ABC, abstractmethod
from datetime import datetime as dt

class newsfeed:
    def __init__(self):
        self.__posts = []

    def add_post(self, post):
        self.__posts.append(post)

    def print_feed(self):
        for p in self.__posts:
                p.display()


class post:
    def __init__(self, author):
        self._author = author 
        self._date = dt.now()

    @abstractmethod
    def display(self):
       pass


class messagepost(post):
    def __init__(self, author, message):
        super().__init__(author)

        self._message = message
  
    def display(self):
         print(f"Date: {self._date} Author: {self._author} Message: {self._message}")

class photopost(post):
    def __init__(self, author, photo):
        super().__init__(author)
        
        self._photo = photo

    def display(self):
         print(f"Date: {self._date} Author: {self._author} Photo: {self._photo}")

feed = newsfeed()
feed.add_post(photopost("Ursula Urlauberin", "photo.jpg"))
feed.add_post(messagepost("Ulf Urlaub", "Ist das Uphuser Meer nicht toll?"))

feed.print_feed()