# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 13:45:36 2020

@author: HjYe
"""
import csv

from Translator.Translator import Translator

class CsvTranslator(Translator):
    def __init__(self):
        self.file_suffix='csv'
        
    def extract_items(self, file):
        csv_file = csv.reader(file)
        items = []
        for item in csv_file:
            items.append(item)
        return items
    
    def append_cfg_item(self, cfg, item):
        cfg[item[0]] = {'value': item[1], 'type': None}
        #or use dataframe form?

if __name__ == '__main__':    
    translator = CsvTranslator()
    s=translator.translate_file('17.csv')
    print(s)