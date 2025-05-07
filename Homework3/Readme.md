# NYCU 2025 spring-Selected Topics in Visual Recognition using Deep Learning Homework3
student id:110652032
name:許元瑞
## Intruduction
This is a implement of digit detection using mask R-CNN pointrend+ResNeXt-101FPN
## How to train?
You can use google colab for quick trianing: https://colab.research.google.com/drive/1-46Wrn8hU46phHKLvf7tR8XJ_NiWpAxM?usp=sharing

1.Put your dataset in google drive with following format

```
 dataset/
    ├── train/
    │   ├── img_name/
    │   │  ├── img1.jpg
    │   │  ├── class1.tif
    │   │  ├── class2.tif
    │   │  └── ...
    └── test/
    │   ├── img1_name.tif
    │   ├── img2_name.tif
    │   └── ...
    └── test_image_name_to_ids.json
```
test_image_name_to_ids.json correspond file_name to ids, height and width.

2.simply run each code for data process,train and predict.

If you want run on your computer. you might need to modify the code and install some dependencies, which is not provide here.

## Performence
leaderboard

![image](https://github.com/user-attachments/assets/88c249ab-53f9-47f7-a65b-785d4bcd473b)






