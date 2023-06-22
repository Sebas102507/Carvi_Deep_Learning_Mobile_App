# Carvi Backend

The app uses two models to achieve this. First, it uses a model called ResNet50, which is a pre-trained convolutional neural network. However, instead of using it directly, the model is fine-tuned to specifically adapt it for the purpose of vehicle recognition. Fine-tuning involves retraining the model using a custom dataset, allowing model weights and features to be tuned to improve its accuracy in the vehicle recognition task. Second, CarVi uses an approach called the Spatial Attention Module (SAM) developed by Meta. SAM is used to remove the "noise" from the captured image of the vehicle, that is, its background and therefore only capture the vehicle. The spatial attention module helps to focus the model's attention on the most important regions of the image, which helps improve the quality and clarity of the information obtained from the vehicle.


<img width="518" alt="Screenshot 2023-06-21 at 10 49 16 PM" src="https://github.com/Sebas102507/Carvi_Deep_Learning_Mobile_App/assets/52805660/44971dc8-6fe1-48e9-8d9b-539c60631878">


<img width="1093" alt="Screenshot 2023-06-21 at 10 48 53 PM" src="https://github.com/Sebas102507/Carvi_Deep_Learning_Mobile_App/assets/52805660/525c97f3-98fd-4e54-97d1-4735b8346dc9">

