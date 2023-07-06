from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import cv2
import numpy as np
from PIL import Image


# Create your views here.
def showIntro():
    print("+++++------------------------------------------------------------------------------------------------+++++")
    print("+++++--------------------------------------CARVI.AI COMPANY -----------------------------------------+++++")
    print("+++++-------------------------------------------Query------------------------------------------------+++++")
    print("+++++-------------------------------------Juan Sebastián V. T.---------------------------------------+++++")
    print("+++++------------------------------------------------------------------------------------------------+++++") 


@csrf_exempt
@api_view(['GET'])
def getCarName(request):
    
        label_number = request.GET.get('label_number')
        
        print(f"Getting file info at: {timezone.localtime(timezone.now())}")
        
        showIntro()
        
        lables_names=pd.read_csv("query/data/cars_labels_names.csv")
        
        car_name = lables_names.loc[int(label_number), 'Car']
        
        car_name=str(car_name)
        
        car_split=car_name.split(" ")
        
        make, model = car_split[0],car_split[1]
        
        print(make)
        
        print(model)
        
        
        url = "https://api.api-ninjas.com/v1/cars"
        headers = {
            "X-Api-Key": "ELrYMUZrcYk6YpcEfpLEMg==SGq8zcEYfO1HyN52"
        }
        params = {
            "limit": 3,
            "make": make.strip(),
            "model": model.strip()
        }

        response = requests.get(url, headers=headers, params=params)

        # Access the response data
        data = response.json()

        # Do something with the data
        print(data)
        
        print(data[1])
        
        selected_car=data[1]
        
        
                        
        return Response({
            'message': 'Hi, welcome to Carvi AI Query Service🚗',
            "class":selected_car["class"],
            "cylinders":selected_car["cylinders"],
            "fuel_type":selected_car["fuel_type"],
            "make":selected_car["make"],
            "model":selected_car["model"],
            "transmission":selected_car["transmission"],
            "year":selected_car["year"]
            },status=status.HTTP_200_OK)
        

