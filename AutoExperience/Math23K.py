#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/24/2022 2:21 PM
# @Author  : Yuming Yan
# @File    : Math23K_tools.py
# @Create Comment  :
import json

from AutoExperience.Models.GPT3 import GPT3


import time
from datetime import datetime
from AutoExperience.Models.utils import get_model
from loguru import logger


def get_data(data_type):

    with open(f"../datasets/math_23K/data_{data_type}.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
        f.close()
    return data

class AutoExpMath23K():
    def __init__(self, parameter):
        self.parameters = parameter.parameters
        self.model = get_model(self.parameters)

    def get_experience_result(self,data_type):
        data = get_data(data_type)

        result_data = []
        for item in data:
            result = dict()
            result['id']=item['id']
            result['original_data']=item
            result['question']=item['original_text']
            result['answer']=item['ans']
            result['model_input'] = self.format_model_input(item, self.parameters['prompt'])
            result['model_output'] = self.model.generate_output(result['model_input'])
            result['model_corrent'] = self.is_model_correct(item, result['model_output'])
            result_data.append(result)

        experience_result = dict()
        #TODO: add more imformation
        experience_result['result_data'] = result_data
        experience_result['accuracy'] = self.calculate_accuracy(data_type, result_data)
        experience_result['datetime'] = datetime.now()

        # TODO: add log(and excel?) to record experience_result
        logger.info(experience_result)
        return experience_result

    def format_model_input(self,data_item, prompt):
        model_input = \
            f'Q:{data_item["original_text"]}' +\
            f'A:{prompt}'
        return model_input

    def is_model_correct(self, data_item, model_output):
        res = False
        if data_item['ans'] in model_output:
            res=True
        return res

    def calculate_accuracy(self, data_type, result_data):
        k = 0
        for item in result_data:
            if item['model_corrent']:
                k += 1

        accuracy=0
        if data_type=='tiny':
            accuracy = k/20
        if data_type=='small':
            accuracy = k/100
        if data_type=='large':
            accuracy = k/500
        if data_type=='all':
            accuracy = k/23162

        return accuracy