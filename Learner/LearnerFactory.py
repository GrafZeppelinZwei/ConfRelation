# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 13:49:52 2020

@author: HjYe
"""

from Learner.MissingLearner import MissingLearner
from Learner.ValueLearner import ValueLearner
from Learner.TypeLearner import TypeLearner

class LearnerFactory:        
    def build_learners(learner_flags, spt_thresh, cfd_thresh):
        learners = []
        if learner_flags['missing']:
            learners.append(LearnerFactory.build_learner(
                    'missing', spt_thresh, cfd_thresh))
        if learner_flags['type']:
            learners.append(LearnerFactory.build_learner(
                    'type', spt_thresh, cfd_thresh))
        if learner_flags['value']:
            learners.append(LearnerFactory.build_learner(
                    'value', spt_thresh, cfd_thresh))
        return learners
    
    def build_learner(type_str, spt_thresh, cfd_thresh):
        if type_str == 'missing':
            learner = MissingLearner(spt_thresh, cfd_thresh)
        elif type_str == 'value':
            learner = ValueLearner(spt_thresh, cfd_thresh)
        elif type_str == 'type':
            learner = TypeLearner(spt_thresh, cfd_thresh)
        else:
            learner = None
        return learner