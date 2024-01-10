from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import Mcq_Serializer, Custom_user_Serializer, Submission_Serializer
from .models import Mcq, Custom_user, Submission

@api_view(['GET'])
def get_mcq(request):
    try:
        question_id = request.query_params.get("id")
        question = Mcq.objects.get(pk=question_id)
        
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
    ans = Mcq.objects.get(pk=question_id)
    return True if ans.correct == option else False

def update_score(user_id, question_id, status):
    user = Custom_user.objects.get(pk=user_id)
    question = Mcq.objects.get(pk=question_id)
    
    if status:
        user.score += question.positive_marks
    else:
        user.score += question.negative_marks

    user.save()


@api_view(['POST'])
def submit(request):
    serializer = Submission_Serializer(data=request.data)
    
    if serializer.is_valid():
        user_instance = serializer.validated_data['user_id']
        mcq_instance = serializer.validated_data['question_id']
        option = serializer.validated_data['selected_option']
        question_id = mcq_instance.question_id
        user_id=user_instance.user_id


        Status = evaluate_mcq(question_id, option)
        update_score(user_id, question_id, Status)
        serializer.validated_data['status']=Status
        serializer.save()  # issue
        return Response(status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


