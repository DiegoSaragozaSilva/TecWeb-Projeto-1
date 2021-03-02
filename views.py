from utils import build_response, load_data, load_template, add_entry

def index(request):
    if request.startswith('POST'):
        request = request.replace('\r', '')
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        for chave_valor in corpo.split('&'):
            splitted = chave_valor.split('=')
            params[splitted[0]] = splitted[1].replace('+', ' ')
        add_entry(params)
        return build_response(code = 303, reason = 'See Other', headers = 'Location: /')

    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    return build_response(load_template('index.html').format(notes=notes))