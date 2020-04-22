#!/usr/bin/python      
# -*- coding: utf-8 -*-     
'''打印文件列表'''
import os
def print_filelist(path):
    """传入一个文件路径，打印该路径下的所有文件和文件夹"""
    try:
        files = os.listdir(path)
        for file in files:
            print(file)
    except:
        print("输入路径不存在")
if __name__=="__main__":
    path = input("请输入文件路径:")
    print_filelist(path)