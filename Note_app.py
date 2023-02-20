import datetime
import json
import re
from Note import Note
from View import *
from constants import *
from Note_list import Note_list


class Note_app:
    def __init__(self):
        self.__notes = Note_list()
        self.__actions = {}
        self.__editing_options = {}
        self.__confirm_options = {}
        self.__editing_functions = {}
        self.__act_functions = {}
        self.__save_functions = {}
        self.__conf_functions = {}

    @property
    def notes(self):
        return self.__notes

    @property
    def actions(self):
        return self.__actions

    @property
    def editing_options(self):
        return self.__editing_options

    @property
    def confirm_options(self):
        return self.__confirm_options

    @property
    def editing_functions(self):
        return self.__editing_functions

    @property
    def act_functions(self):
        return self.__act_functions

    @property
    def save_functions(self):
        return self.__save_functions

    @property
    def conf_functions(self):
        return self.__conf_functions

    @notes.setter
    def notes(self, notes):
        self.__notes = notes

    @actions.setter
    def actions(self, actions):
        self.__actions = actions

    @editing_options.setter
    def editing_options(self, editing_options):
        self.__editing_options = editing_options

    @confirm_options.setter
    def confirm_options(self, confirm_options):
        self.__confirm_options = confirm_options

    @editing_functions.setter
    def editing_functions(self, editing_functions):
        self.__editing_functions = editing_functions

    @act_functions.setter
    def act_functions(self, act_functions):
        self.__act_functions = act_functions

    @save_functions.setter
    def save_functions(self, save_functions):
        self.__save_functions = save_functions

    @conf_functions.setter
    def conf_functions(self, conf_functions):
        self.__conf_functions = conf_functions

    # functions for act_functions dict

    def add_note(self):
        self.__notes.add_note(self.__notes.create_note(
            View.get_value(INPUT_TITLE), View.get_value(INPUT_BODY)))
        View.print_msg(ADD % Note_list.counter)

    def edit_notes(self):
        id = self.get_id()
        option = Note_app.get_option(
            self.__editing_options, SELECT_ALT, INCOR_DATA)
        for key, value in self.__editing_functions.items():
            if key == option:
                value(id)

    def print_notes_by_date(self):
        self.print_by_date(Note_app.get_date())

    def load_from_file(self):
        self.load_notes(View.get_value(INPUT_FILE_NAME))

    def del_note(self):
        id = self.get_id()
        self.__notes.del_note(id)
        View.print_msg(DEL_NOTE % id)

    def print_note_list(self):
        View.print_msg(DELIMITER)
        for i in self.__notes.note_list:
            Note_app.print_note(i)
            View.print_msg(DELIMITER)

    def write_notes(self):
        try:
            with open("notes.json", 'w') as data:
                res = []
                for i in self.notes.note_list:
                    res.append(i.__dict__)
                data.write(json.dumps(res, indent=4))
            View.print_msg(WRITE_NOTE)
        except OSError:
            View.print_msg(ERROR_WRITE_IN)

    # functions for editing_functions dict

    def edit_title(self, id):
        self.__notes.edit_title(id, View.get_value(NEW_DATA))
        View.print_msg(EDIT_TITLE)

    def edit_body(self, id):
        self.__notes.edit_body(id, View.get_value(NEW_DATA))
        View.print_msg(EDIT_BODY)

    # functions for conf_functions & save_functions dict

    def quit_confirm(self):
        choice_num = Note_app.get_option(
            self.__confirm_options, CONTINUE, INCOR_DATA)
        Note_app.select_from_dict(self.__conf_functions, choice_num)

    def save_confirm(self):
        choice_num = Note_app.get_option(
            self.__confirm_options, SAVE, INCOR_DATA)
        Note_app.select_from_dict(self.__save_functions, choice_num)

    # support functions

    def get_id(self):
        id = View.get_value(INPUT_ID)
        if self.__notes.check_id(id) != True:
            View.print_msg(INCOR_DATA)
            id = self.get_id()
        return id

    def get_date():
        date = View.get_value(INPUT_DATE)
        if re.match(REGEX, date) == None:
            View.print_msg(INCOR_FORMAT)
            date = Note_app.get_date()
        return date

    def select_from_dict(dict, option):
        for key, value in dict.items():
            if key == option:
                value()

    def dict_to_str(dict):
        str = ''
        for key, value in dict.items():
            str += f'{key} - {value}\n'
        return str

    def get_option(dict, str, err_str):
        View.print_msg(str)
        option = View.get_value(Note_app.dict_to_str(dict))
        if option in dict.keys():
            return option
        else:
            View.print_msg(err_str)
            option = Note_app.get_option(dict, str, err_str)
            return option

    def print_by_date(self, date):
        y = int(date[:4])
        m = int(date[5:7])
        d = int(date[8:])
        for i in self.notes.note_list:
            if datetime.datetime.strptime(i.date[:10], '%d-%m-%Y') == datetime.datetime(y, m, d):
                Note_app.print_note(i)
                View.print_msg(DELIMITER)

    def load_notes(self, file_name):
        try:
            with open(file_name, 'r') as data:
                nl = Note_list()
                l = json.load(data)
                for i in l:
                    n = Note()
                    n.__dict__ = i
                    nl.add_note(n)
                self.notes = nl
                print(self.notes.note_list[-1].id)
                Note_list.counter = self.notes.note_list[-1].id
            View.print_msg(LOAD_FROM_FILE)
        except FileNotFoundError:
            View.print_msg(FILE_NOT_FOUND)
        except OSError:
            View.print_msg(READ_ERROR)

    def print_note(note):
        View.print_msg(f'{note.id}\n{note.title}\n{note.body}\n{note.date}')

    # main

    def run(self):
        action = Note_app.get_option(self.__actions, SELECT_ACTION, INCOR_DATA)
        Note_app.select_from_dict(self.__act_functions, action)
        self.quit_confirm()
