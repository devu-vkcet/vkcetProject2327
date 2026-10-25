from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('students.db')
    conn.execute('CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, rollno TEXT, course TEXT, backlogs TEXT)')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    conn = sqlite3.connect('students.db')
    students = conn.execute('SELECT * FROM student').fetchall()
    conn.close()
    return render_template('index.html', students=students)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    rollno = request.form['rollno']
    course = request.form['course']
    backlogs = request.form['backlogs']
    conn = sqlite3.connect('students.db')
    conn.execute('INSERT INTO student (name, rollno, course, backlogs) VALUES (?,?,?,?)', (name, rollno, course, backlogs))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect('students.db')
    conn.execute('DELETE FROM student WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/delete_last')
def delete_last():
    conn = sqlite3.connect('students.db')
    conn.execute('DELETE FROM student WHERE id = (SELECT MAX(id) FROM student)')
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

































