from flask import Flask, render_template, request, redirect
import sqlite3
import ctypes
import os

app = Flask(__name__)

# Load the compiled C encryption module
lib = ctypes.CDLL('./encrypt.so')  # Use 'encrypt.dll' on Windows

# Define C function signatures
lib.encrypt.argtypes = [ctypes.c_char_p]
lib.encrypt.restype = ctypes.c_char_p

lib.decrypt.argtypes = [ctypes.c_char_p]
lib.decrypt.restype = ctypes.c_char_p

# Database setup
DB_PATH = 'database.db'

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL
            )
        ''')

@app.route('/')
def index():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute('SELECT id, content FROM notes')
        notes = [
            {'id': row[0], 'content': lib.decrypt(row[1].encode()).decode()}
            for row in cursor.fetchall()
        ]
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['POST'])
def add_note():
    raw_content = request.form['note']
    encrypted = lib.encrypt(raw_content.encode()).decode()

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('INSERT INTO notes (content) VALUES (?)', (encrypted,))
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
