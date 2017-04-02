# -*- coding: utf-8 -*-
import sys
import file_works
from if_opt_equals import if_opt_eqs

reg_list = [0]

mem_list = []


def ready_to_run(opt_list_with_line_num):
    try:
        print("###########Run Prepare###########")
        for opt in opt_list_with_line_num:
            if_opt_eqs(opt, reg_list)

    except Exception as e:
        print("############Exception main############")
        print(e)
        print("############Exception main############")
if __name__ == '__main__':
    opt_list_with_line_num = file_works.file_to_edit_ver('E:\workSpace\mips_translator\\file_in.txt')
    ready_to_run(opt_list_with_line_num)
    print("###########Run Over##############")
