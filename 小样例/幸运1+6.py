#!/usr/bin/python      #告诉Linux/OS 系统这是一个可执行程序，Windows省略
# -*- coding: utf-8 -*-     #指定字符编码
'''幸运1+6
在1~49个数字中随机抽取7个数字，且保证不重复'''

import random

lists = [x for x in range(1,50)]
lucky_numbers = []
for i in range(7):
    lucky_number = random.choice(lists)
    lucky_numbers.append(lucky_number)
    lists.remove(lucky_number)
print(lucky_numbers)
    