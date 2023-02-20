import datetime
from constants import DATE_FORMAT


class Note:
    def __init__(self):
        self.__id = 0
        self.__title = ''
        self.__body = ''
        self.__date = datetime.datetime.now().strftime(DATE_FORMAT)

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @property
    def body(self):
        return self.__body

    @property
    def date(self):
        return self.__date

    @id.setter
    def id(self, id):
        self.__id = id

    @title.setter
    def title(self, title):
        self.__title = title

    @body.setter
    def body(self, body):
        self.__body = body

    @date.setter
    def date(self, date):
        self.__date = date
