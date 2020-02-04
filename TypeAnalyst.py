# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 12:41:12 2020

@author: 51974
"""

import re

class TypeAnalyst:
    patterns = {'int': re.compile("^\d+$"),
                'size': re.compile("^\d+(([K|M|G|T]B?)|B)$"),}
    thresh = 0.9
    
    def is_typeof(type_str, value):
        pattern = TypeAnalyst.patterns[type_str]
        if pattern.match(value) != None:
            return True
        else:
            return False

    def analysis_type(data, key):
        tot = 0
        prob_type = {'int':0, 'size':0}
        for record in data:
            if key not in record.keys():
                continue
            tot += 1
            value = record[key]['value']
            for type_str in TypeAnalyst.patterns:
                if not TypeAnalyst.is_typeof(type_str, value):
                    continue
                prob_type[type_str] += 1
        
        for key in prob_type:
            prob_type[key] = 1.*prob_type[key]/tot
        basic_type = TypeAnalyst.prob2basic(prob_type)
        return basic_type
    
    def prob2basic(prob_type):
        max_num = max(prob_type.values())
        if max_num<TypeAnalyst.thresh:
            return 'str'
        for k, v in prob_type.items():
            if v == max_num:
                return k
    
if __name__ == '__main__':   
    print(TypeAnalyst.is_typeof('int', '1000'))
    print(TypeAnalyst.is_typeof('int', '0'))
    print(TypeAnalyst.is_typeof('int', '100.0'))
    print(TypeAnalyst.is_typeof('size', '20M'))
    print(TypeAnalyst.is_typeof('size', '20KB'))
    print(TypeAnalyst.is_typeof('size', '20B'))
    print(TypeAnalyst.is_typeof('size', '20MK'))

        