# -*- coding: utf-8 -*-
import sys
from antlr4 import *
from AntlrLexer import AntlrLexer
from AntlrParser import AntlrParser
from AntlrListener import AntlrListener
import zipfile
import os
import codecs
import time
# from numba import jit
from timeit import timeit
import json

def unzip_scratch(filename):
    """
    unzip scratch project and extract project.json file   
    :param filename: filename fo scratch project 
    :return: null or project.json content
    """
    zfile = zipfile.ZipFile(filename, 'r')
    if "project.json" in zfile.namelist():
        data = zfile.read("project.json")
        return data
    else:
        return None

def gen(argv):
    raw_json = unzip_scratch(argv)
    encoded_json = codecs.decode(raw_json, 'utf-8', 'strict')
    input = InputStream(encoded_json)
    if not input:
        return
    lexer = AntlrLexer(input)
    stream = CommonTokenStream(lexer)
    parser = AntlrParser(stream)
    tree = parser.json()
    walker = ParseTreeWalker()
    listener = AntlrListener()
    walker.walk(listener, tree)
    # print(listener.score)
    return listener.score,listener.hint,listener.profile
 
if __name__ == '__main__':
    gen(sys.argv[1])
    # result = {}
    # rootdir = '/home/wxl/hb/test/test_file'
    # list = os.listdir(rootdir)
    # for i in range(0, len(list)):
    #     if(i>100):
    #         break
    #     path = os.path.join(rootdir, list[i])
    #     if os.path.isfile(path):
    #         try:
    #             during = timeit(stmt="gen(path)", setup="from Gen import gen;from __main__ import path", number=1)
    #             result[path] = during
    #         except Exception as e:
    #             print(Exception)
    # r = json.dumps(result)
    # with open("cost_time_antlr.json", 'w') as f:
    #     f.write(r)
