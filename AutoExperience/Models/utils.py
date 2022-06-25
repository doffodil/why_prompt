# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : utils.py
# Time       ：2022/6/25 0:40
# Author     ：Yuming Yan
# version    ：python 3.8
# Description：
"""
from AutoExperience.Models.GPT3 import GPT3

def get_model(parameters):
    if parameters['model'] == 'GPT3':
        model = GPT3(parameters)
        return model