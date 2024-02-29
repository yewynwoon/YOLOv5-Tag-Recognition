# YOLOv5 Employee Tag Recognition

## Overview

This repository contains code for training a YOLOv5 model to recognize employees with a special tag in images or videos. The model is trained on a custom dataset containing images or frames from videos where employees with the special tag are annotated.

## Dataset Preparation

1. **Gathering Data and Annotation**: For data gathering, I used CVAT.ai (https://www.cvat.ai/) to annotate every frame in the 57 second video provided where the employee's tag is visible while making sure not to annotate any frames where the tag's pattern is not clearly visible. Every frame where the tag is visible is annotated with a bounding box around the tag itself only to ensure the model learns to recognise the pattern of the tag rather than the person wearing the tag to avoid bias towards this specific video.

2. **Data Augmentation and Preprocessing**: I then used Roboflow (https://roboflow.com/) to preprocess and augment the frames of the video to prepare them as input for the model. Due to the small amount of data provided, augmentation was required as a way to increase the diversity of the training dataset and improve the model. Even though YOLOv5 has its own augmentation parameters, I added a Flip and Rotation (-+13 degrees) augmentation to simulate what the tag would be like in other videos.

4. **Data Splitting**: For Data Splitting, I used an 80/20 split for training and validation. 

## Model Training

For the model training, I used the pre-trained model of YOLOv5s, one of the main reasons for using this model particular model was its speed and its low complexity compared to other models such as the YOLOv5m which might struggle considering our small and limited dataset.

I trained the model with a batch size of 16 and an initial epoch value of 25 with the default SGD optimiser. This resulted in poor precision and mAP50 values, however, I also noticed the losses were decreasing steadily. For the next couple of runs, I switched to 175 epochs and changed the optimiser to AdamW. These settings produced adequate results, with the precision going as high as 0.86 and the mAP50 at 0.89.

Below is the script used to run the model (provided in footfall_task.ipynb)

```python
run(data='../data.yaml' , weights='yolov5s.pt', img=640, epochs=3, batch_size=16 , name=RES_DIR, optimizer = 'AdamW')
```

Below is the graph produced at the end of the 175 epochs
![alt text](https://github.com/yewynwoon/footfall_task/blob/master/results.png)

As seen above, the loss rates steadily decreased with every epoch and the precision,recall and mAP values increased tremoundously. The cls_loss value stays at zero due to there only being one class.

## Inference
For inference, I used a script I wrote called label_script.py which copies all the frames in the validation folder that contains a tag due to the sparse number of frames containing any tags at all, it made it hard to test inference. 

![alt text](https://github.com/yewynwoon/footfall_task/blob/master/example_image_inference.jpg)

As seen above, the model is able to detect the tag at a 0.6 confidence.

![alt text](https://github.com/yewynwoon/footfall_task/blob/master/example_double_tag.jpg)

Although, sometimes the model would detect small white parts in the frames as the tag due to the poor picture quality.

I also tested the model on the initial video sample.mp4, where it was able to detect the employee moving around with no issues. With the use of the detect.py file in YOLOv5 I was also able to output the object detection data to a txt file that I saved in inference_{inference iteration}/labels where the class, x coordinates, y coordinates, width, height and confidence are given as shown below.

![alt text](https://github.com/yewynwoon/footfall_task/blob/master/inference_output.jpg)

Through this txt file, I was able to output the frame number and the xy coordinates after calculating the absolute pixels with a function to produce a dictionary with the following output:

![alt text](https://github.com/yewynwoon/footfall_task/blob/master/frame_number.jpg)