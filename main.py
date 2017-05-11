# -*- coding: utf-8 -*-
import os
import subprocess
import threading
from inspect import trace

import bishe
import file_works
from if_opt_equals import  if_opt_eqs_func

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


def main(opt_list_with_line_num, debug_flag=None):
    # opt_list_with_line_num = file_works.file_to_edit_ver(filename)
    # run_main(opt_list_with_line_num)
    try:
        print("###########Run Prepare###########")
        for opt in opt_list_with_line_num:
            if_opt_eqs_func(opt, reg_list, mem_list, opt_list_with_line_num)
        if debug_flag:
            for opt in opt_list_with_line_num:
                debug_mode(opt_list_with_line_num, opt)
            # parent_pid = os.getpid()
            # import psutil
            # p = psutil.Process(parent_pid)
            # print('Process status : %s' % p.status())
            # print("my pid is %s " % parent_pid)
            # debug_job = bishe.Job()
             # debug_job.pause()

        # if debug_flag
    except Exception as e:
        print(e)
        print(trace())
        print("############Exception main############")
    # receive_signal()


def debug_mode(opt_list_with_line_num):
    # opt_list_with_line_num = file_works.file_to_edit_ver(filename)
    # run_main(opt_list_with_line_num)
    try:
        print("###########Run Prepare###########")
        for opt in opt_list_with_line_num:
            if_opt_eqs_func(opt, reg_list, mem_list, opt_list_with_line_num)
            parent_pid = os.getpid()
            import psutil
            p = psutil.Process(parent_pid)
            print('Process status : %s' % p.status())
            print("my pid is %s " % parent_pid)
            # opt = opt
            debug_job = bishe.Job(opt_list_with_line_num, opt, reg_list, mem_list)
            debug_job.pause()

    except Exception as e:
        print(e)
        print(trace())
        print("############Exception main############")

def print123():
    for i in range(0, 7):
        print(i)
