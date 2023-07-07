import base64
import io
from django.http import FileResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import cv2
import numpy as np
from PIL import Image
import requests
from carvi_classification.ML.CarviModel import CarviModel

baseSamPath="http://sam-service:9011"
baseQuery="http://query-service:9012"
carviModel=CarviModel()

# Create your views here.
def showIntro():
    print("+++++------------------------------------------------------------------------------------------------+++++")
    print("+++++--------------------------------------CARVI.AI COMPANY -----------------------------------------+++++")
    print("+++++------------------------------------------------------------------------------------------------+++++")
    print("+++++-------------------------------------Juan Sebastián V. T.---------------------------------------+++++")
    print("+++++------------------------------------------------------------------------------------------------+++++") 


@csrf_exempt
@api_view(['GET'])
def sayHi(request):
        
        print(f"Getting file info at: {timezone.localtime(timezone.now())}")
        
        showIntro()
        
        url = f"{baseSamPath}/sam/sayHi/"
        
        response = requests.get(url)
        if response.status_code == 200:
                json_data = response.json()
                print("JSON response:")
                print(json_data)
                
        return Response({'message': 'Hi, welcome to Carvi AI 🚗'},status=status.HTTP_200_OK)
        



@csrf_exempt
@api_view(['POST'])
def getCarModel(request):
        
        print(f"Getting file info at: {timezone.localtime(timezone.now())}")
        
        showIntro()
        
        image =  request.data['image']
        
        print(type(image))
        
                
        seg_url = f"{baseSamPath}/sam/getSegmentedImage/"
        
        seg_response = requests.post(seg_url,files={'image': image})
        if seg_response.status_code == 200:
          json_data = seg_response.json()
          label,seg_image= carviModel.getImageModelPrediction(json_data["seg_image"])
          pillow_image = Image.fromarray(seg_image)          
          buffer = io.BytesIO()
          pillow_image.save(buffer, format='JPEG')      
          mg_str = base64.b64encode(buffer.getvalue())
                    
          query_url=f"{baseQuery}/query/getCarName"
          query_response = requests.get(query_url,params={"label_number":label})
          
          if query_response.status_code == 200:
             json_data = query_response.json()
             return Response({
                     'message': 'The service is working 🚗',
                        "class":json_data["class"],
                        "cylinders":json_data["cylinders"],
                        "fuel_type":json_data["fuel_type"],
                        "make":json_data["make"],
                        "model":json_data["model"],
                        "transmission":json_data["transmission"],
                        "year":json_data["year"],
                     "seg_image":mg_str},status=status.HTTP_200_OK)
        
        
        return Response({'message': 'Error'},status=status.HTTP_400_BAD_REQUEST)
        
        
