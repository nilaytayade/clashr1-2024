from rest_framework import serializers
from .models import Mcq,Custom_user,Submission,User

class Mcq_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Mcq
        fields =['question_id','question_md','a','b','c','d','correct','author','authors_note']

class Custom_user_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Custom_user
        fields =['username','score','current_question','previous_question']


class Submission_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['submission_id','user_id','question_id','selected_option','status']
        

# serializers.py
from rest_framework import serializers




class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
