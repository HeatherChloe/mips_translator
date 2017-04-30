# -*- coding: utf-8 -*-
from inspect import trace

import file_works
from if_opt_equals import  if_opt_eqs_func

reg_list = []
for i in range(0, 32):
    reg_list.append(0)

mem_list = {}


def run_main(opt_list_with_line_num):
    try:
        print("###########Run Prepare###########")
        for opt in opt_list_with_line_num:
            if_opt_eqs_func(opt, reg_list, mem_list, opt_list_with_line_num)
        print(reg_list)
        print(mem_list)
    except Exception as e:
        print(e)
        print(trace())
        print("############Exception main############")


def main(filename):
    opt_list_with_line_num = file_works.file_to_edit_ver(filename)
    run_main(opt_list_with_line_num)

