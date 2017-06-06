# -*- coding: utf-8 -*-
import os
import subprocess
import threading
from inspect import trace

import ui
import file_works
from if_opt_equals import  if_opt_eqs_func
# from thread_works import Job

reg_list = []
for i in range(0, 32):
    reg_list.append(0)

mem_list = {}

opt_list_with_line_num = []


# def run_main(opt_list_with_line_num, debug_job):


def to_opt_list(filename):
    global opt_list_with_line_num
    opt_list_with_line_num = file_works.file_to_edit_ver(filename)
    return opt_list_with_line_num


def main(opt_list_with_line_num):
    try:
        print("###########Run Prepare###########")
        for opt in opt_list_with_line_num:
            if_opt_eqs_func(opt, reg_list, mem_list, opt_list_with_line_num)

    except Exception as e:
        print(e)
        print(trace())
        print("############Exception main############")
