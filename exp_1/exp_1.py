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
exp1_parameter = Parameter(
    prompt='',
    greedy=True
)
exp1 = AutoExpMath23K(exp1_parameter)
exp1_result = exp1.get_experience_result(data_type='tiny')
print(exp1_result) # TODO: Better display
print()