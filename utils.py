import os
import json

def extract_route(request):
    start_index = 3
    end_index = 0
    for i in range(start_index + 1, len(request)):
        if request[i] == ' ':
            end_index = i
            break
    return request[start_index + 2 : end_index]

def read_file(path):
    extensions = ['.txt', '.css', '.html', '.js']

    name, extension = os.path.splitext(path)

    if(extension in extensions):
        file_path = name + extension
        with open(file_path, 'r') as file:
            return file.read()
    else:
        file_path = name + extension
        with open(file_path, 'rb') as file:
            return file.read()

def load_data(path):
    full_path = 'data/' + path
    with open(full_path, 'r') as file:
        return json.loads(file.read())

def load_template(path):
    full_path = 'templates/' + path
    with open(full_path, 'r') as file:
        return file.read()

def add_entry(note):
    path = 'data/notes.json'
    with open(path, 'r+') as file:
        content = json.loads(file.read())
        content.append(note)
        file.seek(0)
        file.truncate()
        json.dump(content, file)

def build_response(body = '', code = 200, reason = 'OK', headers = ''):
    if len(headers) > 0:
        return f'HTTP/1.1 {code} {reason}\n{headers}\n\n{body}'.encode()
    return f'HTTP/1.1 {code} {reason}\n\n{body}'.encode()
