from rest_framework import serializers



class S_Mark_Serializer(serializers.Serializer):
    name = serializers.CharField()
    surname = serializers.CharField()
    subject = serializers.CharField()
    mark = serializers.IntegerField()

class S_Student_Serializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    surname = serializers.CharField()

class S_Subject_Serializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    teacher = serializers.CharField()

class IDSerializer(serializers.Serializer):
    id = serializers.IntegerField()

