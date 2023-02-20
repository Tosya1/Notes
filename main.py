import sys
from Note_app import *

app = Note_app()

app.actions = {
    '1': 'Добавить заметку',
    '2': 'Редактировать заметку',
    '3': 'Просмотеть заметки за конкретную дату',
    '4': 'Загрузить заметки из файла',
    '5': 'Удалить заметку',
    '6': 'Просмотреть список заметок',
    '7': 'Записать в файл'
}

app.editing_options = {
    '1': 'изменение заголовка',
    '2': 'изменение тела заметки'
}

app.confirm_options = {
    '1': 'Да',
    '2': 'Нет'
}

app.act_functions = {
    '1': app.add_note,
    '2': app.edit_notes,
    '3': app.print_notes_by_date,
    '4': app.load_from_file,
    '5': app.del_note,
    '6': app.print_note_list,
    '7': app.write_notes
}

app.save_functions = {
    '1': app.write_notes,
    '2': sys.exit

}

app.editing_functions = {
    '1': app.edit_title,
    '2': app.edit_body
}

app.conf_functions = {
    '1': app.run,
    '2': app.save_confirm
}

app.run()
