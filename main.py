# -*- coding: utf-8 -*-
import sys
from inspect import trace

import file_works
from if_opt_equals import if_opt_eqs

reg_list = []
for i in range(0, 32):
    reg_list.append(0)

mem_list = {}

def show_result():
    pass


def show_reg():
    return str(reg_list)


def show_mem():
    return str(mem_list)

def ready_to_run(opt_list_with_line_num):
    try:
        print("###########Run Prepare###########")
        for opt in opt_list_with_line_num:
            if_opt_eqs(opt, reg_list, mem_list, opt_list_with_line_num)
    except Exception as e:
        print(e)
        print(trace())
        print("############Exception main############")


def main():
    opt_list_with_line_num = file_works.file_to_edit_ver('E:\workSpace\mips_translator\\file_in.txt')
    ready_to_run(opt_list_with_line_num)

