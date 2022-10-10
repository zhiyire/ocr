#-*- coding:utf-8 -*-
#'''
# Created on 18-12-11 上午10:09
#
# @Author: Greg Gao(laygin)
#'''
import os



# base_dir = 'path to dataset base dir'
base_dir = './images'
img_dir = os.path.join(base_dir, 'VOC2007_text_detection/JPEGImages')
xml_dir = os.path.join(base_dir, 'VOC2007_text_detection/Annotations')

icdar17_mlt_img_dir = 'D:/ocr/pic/'
icdar17_mlt_gt_dir = 'D:/ocr/gt/'
num_workers = 0
pretrained_weights = '../../checkpoints/CTPN.pth'
#'D:/BaiduNetdiskDownload/ocr/train_code/train_ctpn/train_data/train_img/'#
#'D:/BaiduNetdiskDownload/ocr/train_code/train_ctpn/train_data/train_label'#

anchor_scale = 16
IOU_NEGATIVE = 0.3
IOU_POSITIVE = 0.7
IOU_SELECT = 0.7

RPN_POSITIVE_NUM = 150
RPN_TOTAL_NUM = 300

# bgr can find from  here: https://github.com/fchollet/deep-learning-models/blob/master/imagenet_utils.py
IMAGE_MEAN = [123.68, 116.779, 103.939]
OHEM = True

checkpoints_dir = '../../checkpoints'
outputs = r'./logs'
