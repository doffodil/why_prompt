# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : data_sample.py
# Time       ：2022/6/22 21:21
# Author     ：Yuming Yan
# version    ：python 3.8
# Description：
"""
import json
import os.path
import random
import pandas as pd

with open("./Math_23K.json", 'r', encoding='utf-8') as f:
    math_23K_data = json.load(f)
    f.close()
data = pd.DataFrame(math_23K_data)
data.id = data.id.astype('int')
if not os.path.exists('./data_tiny.json'):
    data_tiny = data.sample(n=20).sort_values(by='id')
    data_tiny.to_json('data_tiny.json', orient="records", force_ascii=False)
if not os.path.exists('./data_smal.json'):
    data_small = data.sample(n=100).sort_values(by='id')
    data_small.to_json('data_smal.json', orient="records", force_ascii=False)
if not os.path.exists('./data_large.json'):
    data_large = data.sample(500).sort_values(by='id')
    data_large.to_json('data_large.json', orient="records", force_ascii=False)

data.to_json('data_all.json', orient="records", force_ascii=False)

print()