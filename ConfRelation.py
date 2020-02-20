# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 22:57:34 2020

@author: HjYe
"""
from IO import parse_input, display, output
from Translator.TranslatorFactory import TranslatorFactory
from Learner.LearnerFactory import LearnerFactory
from GraphAnalyst.GraphAnalyst import ConfGraph

class ConfRelation:
    def __init__(self, input_info):
        self.translator = TranslatorFactory.build_translator(input_info.cfg_type)
        #print(translator.__class__)
        self.learners = LearnerFactory.build_learners(input_info.learner_flags,
                                   input_info.spt_thresh, input_info.cfd_thresh)
        
    def work(self):        
        data = self.translator.translate_folder(input_info.folder_path)
        #for d in data:
        #    print(d)
        rules = []
        for learner in self.learners:
            rules.append(learner.learn(data))
        
        rules_ = []
        for rs in rules:
            for rule in rs['rules']:
                rules_.append(rule)
        graph = ConfGraph(rules_)
        for rule in rules_:
            rule.importance = graph.compute_importance(rule)
        display(rules)
        output(input_info.output_path, rules)
    
if __name__ == "__main__":
    input_info = parse_input()
    worker = ConfRelation(input_info)
    worker.work()