#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time:2018/5/7
# @File:test.py

import re, os

txt_path = os.path.join(os.getcwd(), '20170426.txt')


def host_pick_content(secstart_flg, secend_flg, start_flg='check disk cpu memory io', end_flg='check connection'):
    with open(txt_path, 'r') as tp:
        tp_rb = tp.read()
        tp_chg = re.sub('-|\d+(rowsselected.)|^Password:|^\n', '', tp_rb)
        tp_pk = re.compile(start_flg + '(.*?)' + end_flg, re.S)
        tp_pkcontent = tp_pk.findall(tp_chg)
    pk_chg = ''.join(tp_pkcontent)
    pk_content = re.compile(secstart_flg + '(.*?)' + secend_flg, re.S)
    tp_result = pk_content.findall(pk_chg)
    tp_result = ''.join(tp_result)
    file_endflg = re.search('\d.\d+\s*%', tp_result).group()
    file_sys_pk = re.compile('(.*?)' + file_endflg, re.S)
    file_sys_space = file_sys_pk.findall(tp_result)
    file_sys_space = ''.join(file_sys_space)
    host_load = re.search('(?P<cpu_load>\d.\d+\s*%)\n(?P<mem_load>\d.\d+%)\n(?P<IO_load>\d.\d+%)', tp_result)
    cpu_load = host_load.group('cpu_load')
    mem_load = host_load.group('mem_load')
    IO_load = host_load.group('IO_load')
    return file_sys_space, cpu_load, mem_load, IO_load


file_jfx1,cpu_jfx1,mem_jfx1,io_jfx1 = host_pick_content('WLWJFX1', 'WLWJFX2')
print(file_jfx1)
print(cpu_jfx1)
print(mem_jfx1)
print(io_jfx1)