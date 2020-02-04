# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 15:05:22 2020

@author: HjYe
"""
import random
import os

class Gen():
    def gen_data(self, folder_path, file_num, method):
        #a->aa1; a->aa2; aa1,aa2->aaa; b->bb; c->cc; a,c->ac
        for i in range(file_num):
            file = open(os.path.join(folder_path,str(i)+'.csv'),'w')
            func = getattr(Gen(), method)
            record = func()
            for item in record:
                file.write(item+"\n")
            file.close()
            
    def gen_missing_record(self):
        #a->aa1; a->aa2; aa1,aa2->aaa; b->bb; a,c->ac
        record = []
        rand = random.randint(0,99)
        if rand<70:
            record.append("a,1")
        rand = random.randint(0,99)
        if rand<60:
            record.append("b,2")
        rand = random.randint(0,99)
        if rand<70:
            record.append("c,3")
        rand = random.randint(0,99)
        if rand<60 and ("a,1" in record):
            record.append("aa1,11")
        rand = random.randint(0,99)
        if rand<60 and ("a,1" in record):
            record.append("aa2,12")
        rand = random.randint(0,99)
        if rand<80 and ("aa1,11" in record) and ("aa2,12" in record):
            record.append("aaa,111")
        rand = random.randint(0,99)
        if rand<60 and ("b,2" in record):
            record.append("bb,22")
        rand = random.randint(0,99)
        if rand<80 and ("a,1" in record) and ("c,3" in record):
            record.append("ac,13")
        return record
    
    def gen_value_record(self):
        #a<aa; b<=bb; c = cc; d >= dd; e>ee
        record = []
        v = {}
        v['a'] = random.randint(0,98)
        v['aa'] = random.randint(v['a']+1,99)
        v['b'] = random.randint(0,99)
        v['bb'] = random.randint(v['b'],99)
        v['c'] = random.randint(0,99)
        v['cc'] = v['c']
        v['d'] = random.randint(0,99)
        v['dd'] = random.randint(0,v['d'])
        v['e'] = random.randint(1,99)
        v['ee'] = random.randint(0,v['e']-1)
        for s in v:
            record.append("%s,%s"%(s, v[s]))
        return record
    
    def gen_missing_value_record(self):
        #a<aa; b<=bb; c = cc; c >= ac; 
        #a->aa; b->bb; c->cc; a,c->ac; aa->aaa
        #-----value-----#
        record = []
        v = {}
        v['a'] = random.randint(0,98)
        v['aa'] = random.randint(v['a']+1,99)
        v['b'] = random.randint(0,99)
        v['bb'] = random.randint(v['b'],99)
        v['c'] = random.randint(0,99)
        v['cc'] = str(v['c'])+'M'
        v['ac'] = random.randint(0,v['c'])
        v['aaa'] = '1MKB'
        #-----missing-----#
        flags=[False,False,False,False]
        if random.randint(0,99)<70:
            flags[0]=True
            record.append("%s,%s"%('a', v['a']))
        if random.randint(0,99)<60:
            flags[1]=True
            record.append("%s,%s"%('b', v['b']))
        if random.randint(0,99)<70:
            flags[2]=True
            record.append("%s,%s"%('c', v['c']))
        if random.randint(0,99)<70 and flags[0]:
            flags[3]=True
            record.append("%s,%s"%('aa', v['aa']))
        if random.randint(0,99)<60 and flags[1]:
            record.append("%s,%s"%('bb', v['bb']))
        if random.randint(0,99)<80 and flags[2]:
            record.append("%s,%s"%('cc', v['cc']))
        if random.randint(0,99)<90 and flags[3]:
            record.append("%s,%s"%('aaa', v['aaa']))
        if random.randint(0,99)<90 and flags[0] and flags[2]:
            record.append("%s,%s"%('ac', v['ac']))
    
        return record
    
gen = Gen()
gen.gen_data("./missingvalue", 100, 'gen_missing_value_record') 