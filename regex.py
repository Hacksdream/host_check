#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time:2018/5/9
# @File:regex.py

import re
str="a b c d"
regex0=re.compile("((\w+)\s+\w+)")
print(regex0.findall(str))
regex1=re.compile("(\w+)\s+\w+")
print(regex1.findall(str))
regex2=re.compile("\w+\s+\w+")
print(regex2.findall(str))