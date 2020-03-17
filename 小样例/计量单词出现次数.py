#!/usr/bin/python      #告诉Linux/OS 系统这是一个可执行程序，Windows省略
# -*- coding: utf-8 -*-     #指定字符编码
'''计量单词出现次数
读取文件，统计单词出现的次数'''

def print_dict(dict):
    """遍历字典"""
    for key in dict:
        print(key,dict[key])

def statistics_words(words):
    """传入单词进行统计数量"""
    d = dict()
    for c in words:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

if __name__ == "__main__":
    words = []    
    with open('words.txt','r') as f:
        words = f.read().split()
    d = statistics_words(words)
    print_dict(d)
    