#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/24/2022 2:21 PM
# @Author  : Yuming Yan
# @File    : Math23K_tools.py
# @Create Comment  :
import json

from Models.GPT3 import GPT3, GPT3Greedy

import logging
import time
from datetime import datetime
logging.basicConfig(filename='Math23K_exp_record.log', level=logging.INFO)


def auto_exp_Math23K(parameters, data_size='tiny'):
    # load data
    with open(f"../datasets/data_{data_size}.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
        f.close()
    # init model
    if parameters.parameters['model'] == "GPT3":
        model = GPT3()



    experience_result = dict()
    experience_result['result_data']=result_data
    experience_result['accuracy'] = accuracy

    record = dict()
    record['model_parameters'] = model.get_parameters()
    record['prompt'] = model.prompt
    record['experience_result'] = experience_result
    record["accuracy"] = 0
    record['timestamp'] = time.time()
    record['datetime'] = str(datetime.now())

    return experience_result
