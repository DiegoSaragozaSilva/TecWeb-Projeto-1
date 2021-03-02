from database import Note
from utils import build_response, delete_from_database, load_data, load_template, add_entry, update_database

def index(request):
    if request.startswith('POST'):
        request = request.replace('\r', '')
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        for chave_valor in corpo.split('&'):
            splitted = chave_valor.split('=')
            params[splitted[0]] = splitted[1].replace('+', ' ')
        print(params)
        if params['type'] == 'create':
            add_entry(params)
        elif params['type'] == 'edit':
            notes = load_data()
            note_to_send = list()
            for note in notes:
                print(f'Title: {note.title} Content: {note.content}\n')
                if note.title == params['org_title'] and note.content == params['org_content']:
                    note_to_send.extend([note.id, params['titulo'], params['detalhes']])
                    break
            update_database(note_to_send)

        elif params['type'] == 'delete':
            notes = load_data()
            id = None
            for note in notes:
                print(f'Title: {note.title} Content: {note.content}\n')
                if note.title == params['org_title'] and note.content == params['org_content']:
                    id = note.id
                    break
            delete_from_database(id)

        return build_response(code = 303, reason = 'See Other', headers = 'Location: /')

    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title = note.title, details = note.content)
        for note in load_data()
    ]
    notes = '\n'.join(notes_li)

    return build_response(load_template('index.html').format(notes=notes))