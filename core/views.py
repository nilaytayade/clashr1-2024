from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import Mcq_Serializer, Custom_user_Serializer, Submission_Serializer
from .models import Mcq, Custom_user, Submission
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



#GLOBAL VARIABLES
POSTIVE_MARKS_1 = 4
POSTIVE_MARKS_2 = 2

NEGATIVE_MARKS_1 = -2
NEGATIVE_MARKS_2 = -1


@api_view(['GET','POST'])
def get_mcq(request):
    try:
        username = request.data["username"]
        user = Custom_user.objects.get(pk=username)
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

def update_score(username, question_id, status):
    user = Custom_user.objects.get(pk=username)

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
        user_instance = serializer.validated_data['username']
        question_id = serializer.validated_data['question_id'].question_id
        option = serializer.validated_data['selected_option']

    
        username = user_instance.username
        Status = evaluate_mcq(question_id, option)
        update_score(username, question_id, Status)

        # Use the Mcq instance instead of its ID before saving it to the Submission model
        serializer.validated_data['status'] = Status
        serializer.save()

        return Response({"status":serializer.validated_data['status']},status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# views.py
# from rest_framework import generics, status
# from rest_framework.response import Response
# from rest_framework_simplejwt.tokens import RefreshToken

# from .serializers import RegistrationSerializer, LoginSerializer



# class RegistrationView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegistrationSerializer

# class LoginView(generics.CreateAPIView):
#     serializer_class = LoginSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data
#         refresh = RefreshToken.for_user(user)
#         return Response({
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         }, status=status.HTTP_200_OK)
