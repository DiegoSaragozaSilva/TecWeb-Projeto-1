import sqlite3

class Note():
    def __init__(self, id = None, title = None, content = ''):
        self.id = id
        self.title = title
        self.content = content

class Database():
    def __init__(self, name):
        self.conn = sqlite3.connect(name + '.db')

        create_string = " CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title STRING, content STRING NOT NULL); "
        self.conn.execute(create_string)

    def add(self, note):
        add_note_string = "INSERT INTO note (title, content) VALUES ('{0}', '{1}');".format(note.title, note.content)
        self.conn.execute(add_note_string)
        self.conn.commit()

    def get_all(self):
        select_string = "SELECT id, title, content from note"
        cursor = self.conn.execute(select_string)

        note_list = list()

        for line in cursor:
            note_list.append(Note(id = line[0], title = line[1], content = line[2]))

        return note_list

    def update(self, entry):
        update_string = "UPDATE note SET title = '{0}' WHERE id = {1};".format(entry.title, entry.id)
        self.conn.execute(update_string)
        update_string = "UPDATE note SET content = '{0}' WHERE id = {1};".format(entry.content, entry.id)
        self.conn.execute(update_string)
        self.conn.commit()
    
    def delete(self, note_id):
        delete_string = "DELETE FROM note WHERE id = {0}".format(note_id)
        self.conn.execute(delete_string)
        self.conn.commit()