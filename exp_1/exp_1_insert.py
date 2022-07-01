#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/24/2022 9:32 AM
# @Author  : Yuming Yan
# @File    : demo.py
# @Create Comment  : 测试不同的prompt在Math23K上的精度表现，统计方式包含greedy和vote两种
import json

from AutoExperience.Parameter import Parameter
from AutoExperience.Math23K import AutoExpMath23K

# set parameters
exp_parameter = Parameter(
    model_type='text-davinci-insert-002',
    prompt='？给出解答：',
    # suffix='所以答案是',
    max_tokens=256,
    greedy=False,
    top_p=1,
    temperature=0.3,
)


class exp_demo(AutoExpMath23K):
    def format_model_input(self, data_item, prompt):
        question = data_item['original_text'][:-1]
        model_iput = f"{question}{prompt}"
        return model_iput


exp = exp_demo(parameter=exp_parameter)

exp_result = exp.get_experience_result(data_type='tiny')
print(exp_result)  # TODO: Better display
print()
