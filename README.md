# Python
1. Multi_Downloader.py
Multi-threaded downloader for downloading image from dataset like OpenImages, ImageNet, etc.

# Machine learning
### 1. Evaluation metrics


# Deep learning
### 1. Image Classification Network : AlexNet, GoogleNet, VGG, Resnet, Desenet
TRAIN :

- INPUT : A lot of image and label of each like : The image is describing DOG, not The image contains DOG

- OUTPUT : A lot of weights (each is float value) in layers (CNN, NN not Maxpool).

TEST :

- INPUT : 1 Image once

- OUTPUT : Predict labels (usual: 10)

### 2. Practising with small dataset
Link : [](https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html)

This link has :

- Training from scratch with simple CNN-FC net : [](./)
- Extracting features map of the input by VGG, then classifying by simple FC
- Use all VGG, make some last layer to be trainable for new data

### 2. Object Detection Network : R-CNN, Fast R-CNN, Faster R-CNN, YOLO, SSD.
TRAIN : 

- INPUT : A lot of image and annotation of each object in the image like : A Dog is located at region with top-left (10, 10), widh=200px, height=300px. A Cat is located another place in the image. And something like that.

- OUTPUT : A lot of weight (of course each value is float) in layers) (CNN, RPN, NN, ..etc)

TEST : 

- INPUT : 1 Image once

- OUTPUT : Which region with top, left position, width, height contains DOG, CAT...

### 3. AP, mAP, IOU, ROC metric
