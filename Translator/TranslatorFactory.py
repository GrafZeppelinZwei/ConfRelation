# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 16:57:37 2020

@author: HjYe
"""
from Translator.CsvTranslator import CsvTranslator

class TranslatorFactory:
    def build_translator(translator_type):
        if translator_type == 'csv':
            translator = CsvTranslator()
        #elif translator_type == 'yaml':
        #    translator = YamlTranslator()
        else:
            translator = None
        return translator