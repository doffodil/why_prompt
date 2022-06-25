#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/24/2022 9:32 AM
# @Author  : Yuming Yan
# @File    : exp_1.py
# @Create Comment  : 测试不同的prompt在Math23K上的精度表现，统计方式包含greedy和vote两种
import json

from Parameter import Parameter
from AutoExperience.Math23K import AutoExpMath23K

# set parameters
exp_parameter = Parameter(
    prompt='',
    greedy=True
)

class exp_demo(AutoExpMath23K):
    def format_model_input(self, data_item, prompt):
        model_iput = f"问题：{data_item['original_text']}\n" \
                     f"答案：按照以下思路作答，"
        return model_iput

exp = exp_demo(parameter=exp_parameter)

exp_result = exp.get_experience_result(data_type='tiny')
print(exp_result) # TODO: Better display
print()