import sqlite3 as sq
from typing import List

from kurs.models import Student,Subject,Mark



def get_con():
    db = sq.connect('kursach.db')
    return db


def db_start():
    db=get_con()
    cur = db.cursor()
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
    db.close()


def add_student(nameSt, sur):
    db=get_con()
    cur = db.cursor()
    cur.execute("INSERT INTO student (name,surname) VALUES (?,?)", (nameSt,sur))
    db.commit()
    cur.execute("""SELECT * FROM student
                        ORDER BY id DESC
                        LIMIT 1""")
    row = cur.fetchone()
    db.close()
    return row

def add_subj(nameSt, tech):
    db=get_con()
    cur = db.cursor()
    cur.execute("INSERT INTO subject (name,teacher) VALUES (?,?)", (nameSt,tech))
    db.commit()
    cur.execute("""SELECT * FROM subject
                    ORDER BY id DESC
                    LIMIT 1""")
    row = cur.fetchone()
    db.close()
    return row

def set_mark(nameSt,surSt,subj,markSt):
    db=get_con()
    cur = db.cursor()
    cur.execute("SELECT * FROM student WHERE name=? AND surname=?", (nameSt,surSt,))
    id_stud = cur.fetchone()[0]
    cur.execute("SELECT * FROM subject WHERE name=?", (subj,))
    id_subj=cur.fetchone()[0]
    cur.execute("INSERT INTO mark (mark,subj,id_student) VALUES ({mark},{subj},{key})".format(mark=markSt,subj=id_subj,key=id_stud))
    db.commit()
    cur.execute("""SELECT * FROM mark
                ORDER BY id DESC
                LIMIT 1""")
    row = cur.fetchone()
    db.close()
    return row


def mapper_show_students(rows):
    tt = []
    for row in rows:
        temp=Student(id=row[0],name=row[1],surname=row[2])
        tt.append(temp)
    return tt
def show_students():
    db=get_con()
    cur = db.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    db.close()
    mapper = mapper_show_students(rows)
    return mapper
def mapper_show_subjects(rows):
    tt : List[Subject] = []
    for row in rows:
        temp=Subject(id=row[0],name=row[1],teacher=row[2])
        tt.append(temp)
    return tt
def show_subjects():
    db=get_con()
    cur = db.cursor()
    cur.execute("SELECT * FROM subject")
    rows = cur.fetchall()
    db.close()
    mapper = mapper_show_subjects(rows)
    return mapper

def mapper_show_student_marks(rows):
    tt : List[Mark] = []
    for row in rows:
        temp=Mark(name=row[0],surname=row[1],subject= row[2],mark=row[3])
        tt.append(temp)
    return tt
def show_student_marks(student_id):
    db=get_con()
    cur = db.cursor()
    cur.execute(""" SELECT s.name AS student_name, s.surname AS student_surname, subj.name AS subject_name, m.mark
    FROM mark m
    JOIN student s ON m.id_student = s.id
    JOIN subject subj ON m.subj = subj.id
    WHERE s.id = ?
    """, (student_id,))
    rows = cur.fetchall()
    print(rows)
    db.close()
    mapper=mapper_show_student_marks(rows)
    return mapper
