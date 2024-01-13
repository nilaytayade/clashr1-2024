from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import Mcq_Serializer, Custom_user_Serializer, Submission_Serializer
from .models import Mcq, Custom_user, Submission



#GLOBAL VARIABLES
POSTIVE_MARKS_1 = 4
POSTIVE_MARKS_2 = 2

NEGATIVE_MARKS_1 = -2
NEGATIVE_MARKS_2 = -1


@api_view(['GET','POST'])
def get_mcq(request):
    try:
        user_id = request.data["user_id"]
        user = Custom_user.objects.get(pk=user_id)
        question_id = user.current_question
        question = Mcq.objects.get(pk=question_id)
        question.correct = "🔒"
        serializer = Mcq_Serializer(question)
        return Response(serializer.data)
    
    except Mcq.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'MCQ not found'})
    
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': str(e)})


@api_view(['GET'])
def get_leaderboard(request):
    all_users = Custom_user.objects.all().order_by('-score')
    serializer = Custom_user_Serializer(all_users, many=True)
    return Response(serializer.data)


def evaluate_mcq(question_id, option):
    ans = Mcq.objects.get(question_id=question_id)
    return True if ans.correct == option else False

def update_score(user_id, question_id, status):
    user = Custom_user.objects.get(pk=user_id)

    if status:
        if user.previous_question:
            user.score += POSTIVE_MARKS_1
        else:
            user.score += POSTIVE_MARKS_2
    else:
        if user.previous_question:
            user.score += NEGATIVE_MARKS_1
        else:
            user.score += NEGATIVE_MARKS_2

    user.previous_question = status
    user.current_question += 1
    user.save()  

   


@api_view(['POST'])
def submit(request):
    serializer = Submission_Serializer(data=request.data)
    
    if serializer.is_valid():
        user_instance = serializer.validated_data['user_id']
        question_id = serializer.validated_data['question_id'].question_id
        option = serializer.validated_data['selected_option']

    
        user_id = user_instance.user_id

        Status = evaluate_mcq(question_id, option)
        update_score(user_id, question_id, Status)

        # Use the Mcq instance instead of its ID before saving it to the Submission model
        serializer.validated_data['status'] = Status
        serializer.save()

        return Response(status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
