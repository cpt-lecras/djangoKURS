from django.db import models

# Create your models here.

class Student:
    id: int
    name: str
    surname: str
    def __init__(self, id: int,name: str,surname: str):
        self.id = id
        self.name=name
        self.surname=surname
class Subject:
    id: int
    name: str
    teacher: str
    def __init__(self, id: int,name: str,teacher: str):
        self.id = id
        self.name=name
        self.teacher=teacher
class Mark:
    name: str
    surname: str
    subject: str
    mark: int
    def __init__(self,name: str,surname: str,subject: str,mark: int):
        self.id = id
        self.name=name
        self.surname=surname
        self.subject=subject
        self.mark=mark