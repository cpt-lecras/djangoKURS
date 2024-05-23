import sqlite3 as sq

db = sq.connect('kursach.db')

cur = db.cursor()


def db_start():
    cur.execute("""CREATE TABLE IF NOT EXISTS student(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    surname TEXT NOT NULL)

    """)
    cur.execute("""CREATE TABLE IF NOT EXISTS mark(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        mark INTEGER NOT NULL,
                        subj INTEGER NOT NULL,
                        id_student INTEGER,
                        FOREIGN KEY(subj) REFERENCES subject (id),
                        FOREIGN KEY(id_student) REFERENCES student (id))

    """)
    cur.execute("""CREATE TABLE IF NOT EXISTS subject(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT ,
                        teacher TEXT NOT NULL)
    """)
    db.commit()

def add_student(nameSt, sur):
    cur.execute("INSERT INTO student (name,surname) VALUES (?,?)", (nameSt,sur))
    db.commit()
    return print("Sucsessfully added")

def add_subj(nameSt, tech):
    cur.execute("INSERT INTO subject (name,teacher) VALUES (?,?)", (nameSt,tech))
    db.commit()
    return print("Sucsessfully added")

def set_mark(nameSt,surSt,subj,markSt):
    cur.execute("SELECT * FROM student WHERE name=? AND surname=?", (nameSt,surSt,))
    id_stud = cur.fetchone()[0]
    cur.execute("SELECT * FROM subject WHERE name=?", (subj,))
    id_subj=cur.fetchone()[0]
    cur.execute("INSERT INTO mark (mark,subj,id_student) VALUES ({mark},{subj},{key})".format(mark=markSt,subj=id_subj,key=id_stud))
    db.commit()
    return print("Sucsessfully added")

def show_students():
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    return rows

def show_subjects():
    cur.execute("SELECT * FROM subject")
    rows = cur.fetchall()
    return rows

def show_student_marks(student_id):
    cur.execute(""" SELECT s.name AS student_name, s.surname AS student_surname, subj.name AS subject_name, m.mark
    FROM mark m
    JOIN student s ON m.id_student = s.id
    JOIN subject subj ON m.subj = subj.id
    WHERE s.id = ?
    """, (student_id,))
    rows = cur.fetchall()
    return rows
