# NYCU 2025 spring-Selected Topics in Visual Recognition using Deep Learning Homework1
student id:110652032
name:許元瑞
## Intruduction
This is a implement of image classification using resnest50d and spinalnet.
## How to train?
You can use google colab for quick trianing: https://colab.research.google.com/drive/1pdwkENNWvU7RvxQS99134aY7QtTxbJKd?usp=sharing

1.Put your dataset.zip in google drive with following format

```
 your_dataset.zip/
    ├── train/
    │   ├── class_001/
    │   │   ├── img1.jpg
    │   │   ├── img2.jpg
    │   │   └── ...
    │   ├── class_002/
    │   │   ├── img1.jpg
    │   │   └── ...
    │   └── ...
    │
    ├── valid/
    │   ├── class_001/
    │   │   ├── img1.jpg
    │   │   └── ...
    │   ├── class_002/
    │   │   ├── img1.jpg
    │   │   └── ...
    │   └── ...
    │
    └── test/
        ├── img1.jpg
        ├── img2.jpg
        └── ...
```
2.simply run each code section for data process,train and predict.

If you want run on your computer. you might need to modify the code and install some dependencies, which is not provide here.

## Performence
leaderboard

![image](https://github.com/user-attachments/assets/0195c316-ac86-4b51-9a6b-d72d62127788)
benchmark

![image](https://github.com/user-attachments/assets/a501cf43-1b01-4805-bc76-408757c477e1)



