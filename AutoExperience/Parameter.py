#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/24/2022 4:34 PM
# @Author  : Yuming Yan
# @File    : Parameters.py
# @Create Comment  :

class Parameter:
    def __init__(self,
                 prompt,
                 model='GPT3',
                 model_type='text-davinci-002',
                 greedy=True,
                 max_out_length=200,
                 top_p=0.5,
                 temperature=0.5,
                 frequency_penalty=0,
                 presence_penalty=0,
                 suffix=None,
                 max_tokens=256,
                 ):

        self.parameters = {
            'model': model,
            'model_type': model_type,
            'greedy': greedy,
            'max_out_length': max_out_length,
            'top_p': 0 if greedy else top_p,
            'temperature': temperature,
            'frequency_penalty': frequency_penalty,
            'presence_penalty': presence_penalty,
            'prompt':prompt,
            'suffix':suffix,
            'max_tokens':max_tokens,
            'best_of': 1,
        }

    def get_all_parameters(self):
        return self.parameters

    def change_parameter(self, key, value):
        # TODO: invalid key
        self.parameters[key] = value
        return self.parameters
