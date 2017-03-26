# -*- coding: utf-8 -*-
import sys
import file_works


order_list = []

reg_list = []

mem_list = []


def ready_to_run(now_name):
    try:
        print("###########Run Prepare###########")
        fp = open(now_name, 'r+')
        if fp is None:
            sys.exit(0)
        fp.close()
    except Exception as e:
        print("############Exception############")
        print(e)
        print("############Exception############")
if __name__ == '__main__':
    now_name = file_works.file_to_edit_ver('E:\workSpace\mips_translator\\file_in.txt')
    ready_to_run(now_name)
    print("###########Run Over##############")
