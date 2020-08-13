from   urllib    import request
from   xml.etree import ElementTree as ET 
from   copy      import copy
from   datetime  import datetime
import time
import argparse

def parse(L): return L[0][out]

def reqproc(url,useragent):
    req = request.Request(url,headers={'User-Agent':useragent})
    req1 = request.urlopen(req).read()
    req2 = ET.fromstring(req1)
    return dictify(req2)

def dictify(r,root=True):
    #This function by Erik Aronesty at stackoverflow
    if root:
        return {r.tag : dictify(r, False)}
    d=copy(r.attrib)
    if r.text:
        d["_text"] = r.text
    for x in r.findall("./*"):
        if x.tag not in d:
            d[x.tag] = []
        d[x.tag].append(dictify(x,False))
    return d

def recdictprint(d):
    for k,v in d.items():
        if isinstance(v,dict):
            recdictprint(v)
        print(k,' : ',v,sep='',end='\n')

out = '_text'
useragent = "Merni's discord bot testing"

def region(name):
    regionnamef = name.lower().replace(' ','_')
    reg_url = 'https://www.nationstates.net/cgi-bin/api.cgi?region='+regionnamef
    reg_d = reqproc(reg_url,useragent)['REGION']    
    num = int(parse(reg_d['NUMNATIONS']))
    dgt = parse(reg_d['DELEGATE'])
    dvt = int(parse(reg_d['DELEGATEVOTES']))
    fdr = parse(reg_d['FOUNDER'])
    flag = parse(reg_d['FLAG'])
    return num,dgt,dvt,fdr,flag






