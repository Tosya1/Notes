import datetime
from Note import Note
from constants import DATE_FORMAT


class Note_list:
    counter = 0

    def __init__(self):
        self.__note_list = []

    @property
    def note_list(self):
        return self.__note_list

    def add_note(self, note):
        self.__note_list.append(note)

    def create_note(self, title, body):
        note = Note()
        Note_list.counter += 1
        note.id = Note_list.counter
        note.title = title
        note.body = body
        return note

    def del_note(self, id):
        for i in self.__note_list:
            if i.id == int(id):
                self.__note_list.remove(i)

    def edit_title(self, id, new_data):
        for i in self.__note_list:
            if i.id == int(id):
                i.title = new_data
                i.date = datetime.datetime.now().strftime(DATE_FORMAT)

    def edit_body(self, id, new_data):
        for i in self.__note_list:
            if i.id == int(id):
                i.body = new_data
                i.date = datetime.datetime.now().strftime(DATE_FORMAT)

    def get_id_list(self):
        id_list = []
        for i in self.note_list:
            id_list.append(i.id)
        return id_list

    def check_id(self, id):
        try:
            if int(id) in self.get_id_list():
                return True
        except ValueError:
            return False
