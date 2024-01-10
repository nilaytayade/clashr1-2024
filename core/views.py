from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import Mcq_Serializer
from .models import Mcq

@api_view(['GET'])
def Get_mcq(request):
    try:
        question_id = request.query_params.get("id")
        question = Mcq.objects.get(pk=question_id)
        
        
        serializer = Mcq_Serializer(question)
        return Response(serializer.data)
    
    except Mcq.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'MCQ not found'})
    
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': str(e)})


@api_view(['POST'])
def test(request):
    return Response(status=status.HTTP_200_OK)