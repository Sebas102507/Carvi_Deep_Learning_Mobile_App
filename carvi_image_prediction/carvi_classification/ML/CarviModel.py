import cv2
import numpy as np
import tensorflow as tf

class CarviModel:

    def __init__(self):
        
        model_path='carvi_classification/ML/carvi_model.h5'
        
        self.model = tf.keras.models.load_model(model_path)
        
        print(self.model.summary())
        
        
    def getImageModelPrediction(self,image):
        
        print("Generating Model Prediction")
        
        image=np.array(image)
        
        image=image.astype(np.uint8)
        
        img_resized = cv2.resize(image, (224, 224), interpolation=cv2.INTER_LINEAR)
        
        img_resized_norm=img_resized/255.
        
        prediction=self.model.predict(np.array([img_resized_norm]))

        print("OK Prediction")

        label=np.argmax(prediction,axis=1)[0]
        
        return label, image 