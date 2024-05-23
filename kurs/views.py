from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from drf_spectacular.utils import extend_schema, extend_schema_view

from .serializers import (
    S_Mark_Serializer,
    S_Student_Serializer,
    S_Subject_Serializer,
    IDSerializer,
)
from .db import (
    add_student,
    add_subj,
    set_mark,
    show_student_marks,
    show_students,
    show_subjects,

)
@extend_schema_view(
    v_add_student=extend_schema(
        summary="Add student",
        responses={
            200: IDSerializer,
            404: None,
        }
    ),
    v_add_subj=extend_schema(
        summary="Add subject",
        responses={
            201: IDSerializer,
            404: None,
        }
    ),
    v_set_mark=extend_schema(
        summary="Set mark",
        responses={
            201: IDSerializer,
            404: None,
        }
    ),
    v_show_students=extend_schema(
        summary="Show students",
        responses={
            201: S_Student_Serializer(many=True),
            404: None,
        }
    ),
    v_show_subjects=extend_schema(
        summary="Show sbj",
        responses={
            201: S_Subject_Serializer(many=True),
            404: None,
        }
    ),
    v_show_student_marks=extend_schema(
        summary="Show marks",
        responses={
            201: S_Mark_Serializer(many=True),
            404: None,
        }
    ),

)
class dbViewSet(ViewSet):
    def v_add_student(self, _, nameSt, sur):
        try:
            meth = add_student(nameSt,sur)
            return Response(f"Access. ID:{meth}")
        except ValueError as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)

    def v_add_subj(self, _, name, teacher):
        try:
            meth = add_subj(name, teacher)
            return Response(f"Access. ID:{meth}")
        except ValueError as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)
    def v_set_mark(self, _, nameSt,surSt,subj,markSt):
        try:
            meth = set_mark(nameSt,surSt,subj,markSt)
            return Response(f"Access. ID:{meth}")
        except ValueError as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)
    def v_show_students(self, _):
        try:
            meth = show_students()
            ser = S_Student_Serializer(meth, many=True)
            return Response(ser.data)
        except ValueError as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)
    def v_show_subjects(self, _):
        try:
            meth = show_subjects()
            ser = S_Subject_Serializer(meth, many=True)
            return Response(ser.data)
        except ValueError as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)
    def v_show_student_marks(self, _, student_id):
        try:
            meth = show_student_marks(student_id)
            ser = S_Mark_Serializer(meth, many=True)
            return Response(ser.data)
        except ValueError as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)