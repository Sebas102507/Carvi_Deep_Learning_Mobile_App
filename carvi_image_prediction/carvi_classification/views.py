from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def showIntro():
    print("+++++------------------------------------------------------------------------------------------------+++++")
    print("+++++--------------------------------------CARVI.AI COMPANY -----------------------------------------+++++")
    print("+++++------------------------------------------------------------------------------------------------+++++")
    print("+++++-------------------------------------Juan Sebastián V. T.---------------------------------------+++++")
    print("+++++------------------------------------------------------------------------------------------------+++++") 

@csrf_exempt
@api_view(['POST'])
def makePrediction(request):
        showIntro()
        print(f"Getting file info at: {timezone.localtime(timezone.now())}")
        return Response({'message': 'The service is working 🚗'},status=status.HTTP_200_OK)
        