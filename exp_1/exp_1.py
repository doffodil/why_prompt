#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/24/2022 9:32 AM
# @Author  : Yuming Yan
# @File    : exp_1.py
# @Create Comment  : 测试不同的prompt在Math23K上的精度表现，统计方式包含greedy和vote两种

from Parameters import Parameters
from AutoExperience.Math23K import auto_exp_Math23K

# set parameters
exp1_parameters = Parameters(
    greedy=True
)
exp1 =
exp1_result = Math23K(exp1_parameters)