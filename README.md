# YOLOv5 Employee Tag Recognition

## Overview

This repository contains code for training a YOLOv5 model to recognize employees with a special tag in images or videos. The model is trained on a custom dataset containing images or frames from videos where employees with the special tag are annotated.

## Dataset Preparation

1. **Gathering Data and Annotation**: For data gathering, I used CVAT.ai (https://www.cvat.ai/) to annotate every frame in the 57 second video provided where the employee's tag is visible while making sure not to annotate any frames where the tag's pattern is not clearly visible. Every frame where the tag is visible is annotated with a bounding box around the tag itself only to ensure the model learns to recognise the pattern of the tag rather than the person wearing the tag to avoid bias towards this specific video.

2. **Data Augmentation and Preprocessing**: I then used Roboflow (https://roboflow.com/) to preprocess and augment the frames of the video to prepare them as input for the model. Due to the small amount of data provided, augmentation was required as a way to increase the diversity of the training dataset and improve the model. Even though YOLOv5 has its own augmentation parameters, I added a Flip and Rotation (-+13 degrees) augmentation to simulate what the tag would be like in other videos.

4. **Data Splitting**: For Data Splitting, I used an 80/20 split for training and validation. 

## Model Training

1. **Installation**: Clone the YOLOv5 repository from https://github.com/ultralytics/yolov5 and install the required dependencies.

2. **Data Formatting**: Organize your dataset in the YOLO format, which consists of a text file for each image or frame containing one row for each annotated object with class index and bounding box coordinates.

3. **Training Configuration**: Configure the training parameters in the `train.py` script, including batch size, number of epochs, learning rate, and model architecture (e.g., YOLOv5s, YOLOv5m).

4. **Model Training**: Run the `train.py` script to start training the YOLOv5 model on your custom dataset. Monitor the training progress and evaluate the model's performance using validation metrics such as loss, precision, recall, and F1-score.

5. **Model Evaluation**: Evaluate the trained model on a separate test set to assess its performance on unseen data. Calculate evaluation metrics such as precision, recall, and F1-score to measure the model's accuracy.

## Inference

1. **Model Deployment**: Deploy the trained model for inference on new images or videos containing employees with the special tag. Use the `detect.py` script to perform inference and visualize the model's predictions.

2. **Integration**: Integrate the model into your application or workflow to automate the process of recognizing employees with the special tag in real-time or batch processing scenarios.

## Conclusion

This codebase provides a framework for training a YOLOv5 model to recognize employees with a special tag in images or videos. By following the steps outlined in this README, you can customize and deploy the model for your specific use case and achieve accurate detection results.

