#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 7/1/2022 10:10 AM
# @Author  : Yuming Yan
# @File    : best-params.py
# @Create Comment  :


# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/24/2022 9:32 AM
# @Author  : Yuming Yan
# @File    : demo.py
# @Create Comment  : 测试不同的prompt在Math23K上的精度表现，统计方式包含greedy和vote两种
import json

from AutoExperience.Parameter import Parameter
from AutoExperience.Math23K import AutoExpMath23K

# set parameters
for p in [0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 0.8, 0.9]:
    exp_parameter = Parameter(
        model_type='text-davinci-002',
        prompt='？求解过程：',
        max_tokens=256,
        greedy=False,
        top_p=1,
        temperature=p,
    )


    class exp_demo(AutoExpMath23K):
        def format_model_input(self, data_item, prompt):
            question = data_item['original_text'][:-1]
            model_iput = f"{question}{prompt}"
            return model_iput


    exp = exp_demo(parameter=exp_parameter)

    exp_result = exp.get_experience_result(data_type='tiny')

    print(
        f'======{p}============================================================')
    print(exp_result)  # TODO: Better display
