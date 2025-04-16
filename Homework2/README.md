
# NYCU 2025 spring-Selected Topics in Visual Recognition using Deep Learning Homework2
student id:110652032
name:許元瑞
## Intruduction
This is a implement of digit detection using fasterrcnn_resnest50_fpn_v2.
## How to train?
You can use google colab for quick trianing: [https://colab.research.google.com/drive/1pdwkENNWvU7RvxQS99134aY7QtTxbJKd?usp=sharing](https://colab.research.google.com/drive/18C2-wLm1E9PEho0H0UzFRn_88uqoHn5Y?usp=sharing)

1.Put your dataset.zip in google drive with following format

```
 SVHN_dataset.zip/
    ├── train/
    │   ├── img1.jpg
    │   ├── img2.jpg
    │   └── ...
    ├── valid/
    │   ├── img1.jpg
    │   ├── img2.jpg
    │   └── ...
    └── test/
    │   ├── img1.jpg
    │   ├── img2.jpg
    │   └── ...
    └── train.json
    └── valid.json
    └── test.json
```
_train.json,valid.json,test.json_ with coco format.
If you don't have test.json. You can run _test_lable.py_ on your computer to generate it.

2.simply run each code for data process,train and predict.

If you want run on your computer. you might need to modify the code and install some dependencies, which is not provide here.

## Performence
leaderboard

![image](https://github.com/user-attachments/assets/3678ca70-40d2-43c4-b8a2-730e03fd1386)





