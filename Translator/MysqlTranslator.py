# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 16:25:49 2020

@author: 51974
"""
import re
from Translator.Translator import Translator

class MysqlTranslator(Translator):
    pattern_comment = re.compile("^#|!.*")
    pattern_namespace = re.compile("^\[.*\]$")
    pattern_config = re.compile("^.*=.*$")
    def __init__(self):
        self.file_suffix='cnf'
        
    def extract_items(self, file):
        items = []
        lines = file.readlines()
        namespace = ''
        for line in lines:
            line = line.replace(' ', '')
            line = line.replace('\t', '').strip()
            if line == '':
                continue
            if MysqlTranslator.pattern_comment.match(line):
                continue
            elif MysqlTranslator.pattern_namespace.match(line):
                namespace = line
            elif MysqlTranslator.pattern_config.match(line):
                line = re.split("#", line)[0]
                item = re.split("=", line)
                item.append(namespace)
                items.append(item)
            else:
                line = re.split("#", line)[0]
                item = [line, 'True', namespace]
                items.append(item)
        return items
    
    def append_cfg_item(self, cfg, item):
        key = item[2]+' '+item[0]
        cfg[key] = {'value': item[1], 'type': None}

if __name__ == '__main__':    
    translator = MysqlTranslator()
    s=translator.translate_file('../aa.cnf')
    print(s)